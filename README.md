# Complaints-Classifier by SOPHO_HACKERS

Concept Theme : Digital Alter Ego 

A complaints classifer for banks built using Python and Amazon Web Services(AWS)

Instructions for use:
* Run : `pip install -r requirement.txt` in Shell to Download all Necessary Packages for running the Application
* Install and Set Up [AWS CLI](https://aws.amazon.com/cli/)
* Configure it with:
`aws configure`
* Add your credentials in the relevant parts of the python scripts-
  * In calling_comprehend: DataAccessRoleArn, DocumentClassifierArn
  * Also in complaintclassifier_train. and spamclassifier_train fill the dataaccessrole arn.

* **Setting up the inputs:**

  * The input audio file(which is the complaint) should be stored as "test-audio-\<number\>.mp3" in the test-audio folder which is inside the folder dbs_app("`.\Complaints-Classifier-application_v1\dbs_app\test-audio`") and they will be classified in the same order.
  * The relevant contact numbers of the customers along with their account numbers should be stored in the csv file in ./Database/Accno_Phno_db.csv (we have added some sample contact number + account number in it).
  
 * Run the complaintclassifier_train. and spamclassifier_train files once to create the classifiers.

**DBS app folder contains the working code, the other files were used for training the comprehend models**

'* **Running the program**
 
 1. Without changing/modifying any files run the python file **driver.py**. When we used a single audio file the program took 10 minutes to finish running and when we used 3 audio files it took approximately 20 minutes to complete.
 
 2. First the given audio is converted into text file using amazon transcribe. A successful call to transcribe will print a json file. Importantly the json file contains the job id and other information regarding the job.
 
 3. This is followed by a series of "Not Ready Yet" messages every 30 seconds till the output is received from AWS. The output is taken from the S3 bucket and is downloaded locally and stored as string variable(s).
 
 4. This text is then passed to the summarization function which summarizes the text in N/2 lines when N>5 where N is the number of lines in the initial complaint(after trying out different bounds on the number of lines like root(N), log(N) etc.) we felt the output for N/2 was better. It uses the NLTK library to do text ranking.
 
 5. The summarized text is then passed to the **Spam Classfier**(which classifies whether the complaint is a spam complaint or not) and the **Complaints Classifier** which classifies the complaint into a category among the 12 different categories we have used.
 
 6. For both the classifiers, a successful call will print a json file and a series of "Not ready yet" messages follow until the output is obtained from AWS.
 
 7. The output is written in a text file named **Outputs.txt** created in the same directory as driver.py
 
 8. The program terminates with the message "Check Outputs.txt".

* The output will be written as a text file "Outputs.txt" in the same folder in the following format for each complaint in order:
  
 SPAM (YES/NO) :

 TYPE OF COMPLAINT/QUERY : 
 
 OTHER ASSOCIATED COMPLAINT/QUERY TAGS : 

 SUMMARY OF COMPLAINT/QUERY : 

 Contact Number of the Customer :

 Matching Account No(s) : 

```
OTHER ASSOCIATED COMPLAINT/QUERY TAGS is meant to display categories that are good enough in describing the complaint/query,
but don't have the maximum score of closeness to the text. Their inclusion will reduce the possibility of any significant errors in prediction. It might sometimes be left empty when there is no other tag which has a good level of accuracy in describing the complaint/query.
```
Brief Descriptions of the files and folders in the GitHub : 

- Training_Dataset : Folder containing Dataset for training the machine learning custom classification models on AWS
  - complaint_train.csv : Dataset for complaint classification model
  - spam_train.csv : Dataset for spam classification model
- complaintclassifier_train.py : Program to train the complaint classification model using the corresponding training Dataset in S3 Bucket "bankcomplaints"
- spamclassifier_train.py : Program to train the spam classification model using the corresponding training Dataset in S3 Bucket "bankcomplaints"
- rootkeysubmission.csv : Contains the access key ID and secret access key to access the machine learning models, transcribe and S3 buckets we created
- requirement.txt : Contains the necessary Python Packages and Modules one need to install before running the program
- submission_sophohackers.pptx : Contains the slides used to make the video
- README.md : (This File) Contains the information and instructions related to setting up the environment,understanding and runnning the spplication
- dbs_app : Folder containing the working code and resources necessary to run the application
  - Database : Folder to mimic a customer database in a bank for representative purposes
    - Accno_Phno_db.csv : File contains Account Number and corresponding Phone Number Details
  - test-audio : Folder contains the Test Audio Files to be run the application on (We have generated 10 test audio files to see how our application runs)
  - calling_comprehend.py : Program which calls the Custom Classification Model we trained in Comprehend of AWS to do the label prediction
  - clean_string.py : Program which cleans a given string of all punctuation marks, and non alphabetic characters
  - driver.py : The Main Program which needs to run. It integrates all other modules and process the test audio files to generate required output in "Outputs.txt" file
  - multiple_tarfile_opener.py : Program which opens a .tar file and extracts the JSON Object from it
  - phno_to_accno.py : Program to get the Account numbers a given Phone Number maps to
  - s2t.py : Program which calls Speech To Text in Transcribe of AWS to convert audio file (here, .mp3 file) to a text file
  - s3_filedownload.py : Program which accesses the S3 Bucket we specify to download a resource from it to Local Storage
  - textsummarization.py : Program which uses TextRank Algorithm and NLTK (Natural Language ToolKit) Library of Python to rank the sentences in a paragraph and extract the essential sentences to summarize the paragraph
  - upload_s3.py : Program to upload a resource from Local Storage to the S3 Bucket we specify
 
