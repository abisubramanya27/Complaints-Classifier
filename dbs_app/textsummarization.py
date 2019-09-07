# =====================================================================================================================================
""" Summarizes Text By Picking the most important sentences using TextRank Algorithm  """
# =====================================================================================================================================

import re
import nltk.tokenize as nt
import numpy as np
import pandas as pd
import math
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('stopwords')
nltk.download('wordnet')
#Functions to calculate tf-idf values to generate vectors for words
def tf(word,wordl):
    return wordl.count(word) / len(wordl)

def contains(word,sentl):
    return sum(1 if sent.find(word) != -1 else 0 for sent in sentl)

def idf(word,sentl):
    return math.log(len(sentl) / contains(word,sentl))

def tfidf(word,wordl,sentl):
    return tf(word,wordl) * idf(word,sentl)

def summarize(txt) :

    #Breaking the text into list of sentences
    txt = txt.replace('\'',' ')
    txt = txt.replace('\"',' ')

    sentl = list(filter(lambda x:x.strip() != "",re.split('[.?!]+',txt)))

    lemmatizer = WordNetLemmatizer()

    #Place in sentl corresponding to sentence in clean_sentl
    place = list(range(len(sentl)))

    #Cleaning up the sentences to only include meaningful words (and avoiding numerics and characters other than alphabets)
    clean_sentl = [re.sub('[^a-zA-Z]+',' ',a).lower() for a in sentl]
    clean_sentl = [' '.join(lemmatizer.lemmatize(w) for w in s.split() if (w is not None and w not in stopwords.words('english'))) for s in clean_sentl]
    tmp_l = []
    for ind,s in enumerate(clean_sentl):
        if s.strip() == "":
            del place[ind]
        else:
            tmp_l.append(s)

    clean_sentl = tmp_l

    #Generating unique list of all words present in all the sentences to run tf-idf on them
    wordslist = [w for s in clean_sentl for w in s.split()]
    wordslist = list(np.unique(np.array(wordslist)))

    #Vectorizing sentences using tf-idf scores for each word in wordslist
    vector_sent = []

    for s in clean_sentl:
        score = []
        wordl = s.split()
        for w in wordslist:
            score.append(tfidf(w,wordl,clean_sentl))
        vector_sent.append(score)
    
    #Obtaining similarity matrix from the vectors of words using cosine_similarity
    similarity_matrix = np.zeros((len(clean_sentl),len(clean_sentl)))
    for i in range(len(clean_sentl)):
        for j in range(len(clean_sentl)):
            if(i != j):
                similarity_matrix[i,j] = cosine_similarity(np.array(vector_sent[i]).reshape(1,-1),np.array(vector_sent[j]).reshape(1,-1))
        if(similarity_matrix[i].sum() == 0):
            similarity_matrix[i] += (1/len(similarity_matrix))
        else:
            similarity_matrix[i] /= similarity_matrix[i].sum()

    #Text Rank Algorithm which executes iteratively till convergence (or for a specified maximum number of times, here 100)
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

    #Sorting the textrank list in descending order of scores so that we pick the most relevant sentences (top sqrt(N) out of N sentences)
    textrank = sorted(textrank,key = lambda x: x[0],reverse = True)

    output_str = ""

    for i in range(int(math.sqrt(len(place)))) :
        output_str += sentl[place[textrank[i][1]]]
        output_str += " ";

    print("\n")
    return output_str

# =========================================================================================================================================
