import re
import nltk.tokenize as nt
import numpy as np
import pandas as pd
import math
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity

def tf(word,wordl):
    return wordl.count(word) / len(wordl)

def contains(word,sentl):
    return sum(1 if sent.find(word) != -1 else 0 for sent in sentl)

def idf(word,sentl):
    return math.log(len(sentl) / contains(word,sentl))

def tfidf(word,wordl,sentl):
    return tf(word,wordl) * idf(word,sentl)

def summarize(txt) :

    txt = txt.replace('\'',' ')
    txt = txt.replace('\"',' ')

    sentl = list(filter(lambda x:x.strip() != "",re.split('[.?!]+',txt)))

    lemmatizer = WordNetLemmatizer()

    place = list(range(len(sentl)))

    clean_sentl = [re.sub('[^a-zA-Z]+',' ',a).lower() for a in sentl]
    clean_sentl = [' '.join(lemmatizer.lemmatize(w) for w in s.split() if (w is not None and w not in stopwords.words('english'))) for s in clean_sentl]
    tmp_l = []
    for ind,s in enumerate(clean_sentl):
        if s.strip() == "":
            del place[ind]
        else:
            tmp_l.append(s)

    clean_sentl = tmp_l

    wordslist = [w for s in clean_sentl for w in s.split()]
    wordslist = list(np.unique(np.array(wordslist)))

    vector_sent = []

    for s in clean_sentl:
        score = []
        wordl = s.split()
        for w in wordslist:
            score.append(tfidf(w,wordl,clean_sentl))
        vector_sent.append(score)

    similarity_matrix = np.zeros((len(clean_sentl),len(clean_sentl)))
    for i in range(len(clean_sentl)):
        for j in range(len(clean_sentl)):
            if(i != j):
                similarity_matrix[i,j] = cosine_similarity(np.array(vector_sent[i]).reshape(1,-1),np.array(vector_sent[j]).reshape(1,-1))
        if(similarity_matrix[i].sum() == 0):
            similarity_matrix[i] += (1/len(similarity_matrix))
        else:
            similarity_matrix[i] /= similarity_matrix[i].sum()

    def TextRank(eps = 0.0001,max_it = 100,d = 0.85):
        p = np.ones(len(clean_sentl)) / len(clean_sentl)
        for i in range(max_it):
            new_p = np.ones_like(p) * (1-d)/len(clean_sentl) + d * (similarity_matrix.T.dot(p))
            delta = abs(new_p-p).sum()
            if delta < eps:
                break
            p = new_p
        return p

    textrank = TextRank()
    textrank = [(score,ind) for ind,score in enumerate(textrank)]

    textrank = sorted(textrank,key = lambda x: x[0],reverse = True)

    output_str = ""

    for i in range(int(math.sqrt(len(place)))) :
        output_str += sentl[place[textrank[i][1]]]
        output_str += " ";

    return output_str
