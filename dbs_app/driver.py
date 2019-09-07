# ===================================================================================================== 
""" The Main Function which Integrates the Different Processes  """
# =====================================================================================================

#Importing Python Files we created
import s2t 
import s3_filedownload
import tarfile_opener
import textsummarization
import calling_comprehend
import upload_s3
import clean_string
import phno_to_accno

#Importing Python Libraries
import json
import os

bucket_name = "audio-complaint"
file_name = "test-audio.mp3"      #The name of audio complaint file you wish to process
path = './'

#Uploads local audio file to S3 Bucket 
upload_s3.upload(path,bucket_name,file_name)

#Utilises Speech to Text from AWS Transcribe  on the S3 audio file and stores the output JSON in S3 Bucket
file_name = s2t.s2t(bucket_name+'/'+file_name)
file_name += '.json'

#Downloads the output JSON of Speech to Text from S3 and stores in Local Storage
s3_filedownload.download_file(bucket_name,file_name)

#Gets the Text obtained from the audio, from the JSON file
input_complaint = ""
with open(path+file_name) as f:
       for line in f:
           data=json.loads(line)
           input_complaint = data["results"]["transcripts"][0]["transcript"]

#Deletes the output JSON file downloaded from Local Storage
os.remove(path+file_name)

#Summarizes the complaint and cleans it for using the trained model on it
summarized_complaint = textsummarization.summarize(input_complaint)
clean_complaint = clean_string.clean(summarized_complaint)

#Writes the cleaned complaint to a .csv file 
with open('./test_complaint.csv','w') as f :
       f.write(clean_complaint)


bucket_name = "complaints-input"
file_name = "test_complaint.csv"

#Uploads the complaint (.csv) file to S3 Bucket
upload_s3.upload(path,bucket_name,file_name)

file_name = "output.tar.gz"
bucket_name = "complaintsoutput"
S3_extension = "complaints-input/test_complaint.csv"

#Calls AWS comprehend to classify the complaint
calling_comprehend.comprehend(S3_extension,"Complaintclassifierv1",bucket_name)

f = open('./Outputs.txt','w')

s3_filedownload.download_file(bucket_name,file_name)
complaint_type = tarfile_opener.tarfile_open(path+file_name)

os.remove(path+file_name)
os.remove(path+'predictions.jsonl')

file_name = "output.tar.gz"
bucket_name = "spamoutput"
S3_extension = "complaints-input/test_complaint.csv"

#Calls AWS comprehend to detect if the complaint is spam or not
calling_comprehend.comprehend(S3_extension,"Spamclassifierv1",bucket_name)

#Outputs if the complaint is spam or not
f.write("SPAM (YES/NO) : ")

s3_filedownload.download_file(bucket_name,file_name)
if(tarfile_opener.tarfile_open(path+file_name).lower() == "spam") :
	f.write("YES")
else :
	f.write("NO")

#Outputs the type of complaint
f.write("\nTYPE OF COMPLAINT : "+complaint_type)

os.remove(path+file_name)
os.remove(path+'predictions.jsonl')

#Outputs the summary of complaint
f.write("\n\nSUMMARY OF COMPLAINT : ")
f.write(summarized_complaint)

#The phone number from which the complaint was registered, which can be tapped
#Here for representative purpose I have assumed a Phone Number
phone_number = "9876543211"

#Outputs the Phone number and Associated Account numbers
f.write("\n\nContact Number of the Complainant :"+phone_number)
f.write("\n"+phno_to_accno.accphmatch(phone_number))

#Outputs the original complaint
f.write("\n\nORIGINAL COMPLAINT : ")
f.write(input_complaint)

f.close()

#Clear the S3 Bucket for future use
import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('audio-complaint')
bucket.objects.all().delete()

bucket = s3.Bucket('complaints-input')
bucket.objects.all().delete()

bucket = s3.Bucket('complaintsoutput')
bucket.objects.all().delete()

bucket = s3.Bucket('spamoutput')
bucket.objects.all().delete()

print("\n\nCheck Outputs.txt File")

# ======================================================================================================
