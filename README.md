# Complaints-Classifier
A complaints classifer for banks built using Python and Amazon Web Services(AWS)

Instructions for use:
* Run : `pip install -r requirements.txt` in Shell to Download all Necessary Packages for running the Application
* Install and Set Up [AWS CLI](https://aws.amazon.com/cli/)
* Configure it with:
`aws configure`
using the access key ID and the secret access key provided in the csv file **rootkeysubmission.csv**. The user ID we have provided have the permission to run Amazon Comprehend, Amazon Transcribe and as well as read/write in our S3 bucket.

* **Setting up the inputs:**

  * The input audio file(which is the complaint) should be stored as "test-audio-\<number\>.mp3" in the test-audio folder and they will be classified in the same order.
  * The relevant contact numbers of the customers along with their account numbers should be stored in the csv file in ./Database/Accno_Phno_db.csv (we have added some sample contact number + account number in it).

**DBS app folder contains the working code, the other files were used for training the comprehend models**

* **Running the program**
 
 1. Without changing/modifying any files run the python file **driver.py**. For each audio file it takes approximately 10 minutes to finish running(includeing the time taken by the classifiers to run).
 
 2. First the given audio is converted into text file using amazon transcribe. A successful call to transcribe will print a json file. Importantly the json file contains the job id and other information regarding the job.
 
 3. This is followed by a series of "Not Ready Yet" messages every 30 seconds till the output is received from AWS. The output is taken from the S3 bucket and is downloaded locally and stored as string variable(s).
 
 4. This text is then passed to the summarization function which summarizes the text in N/2 lines when N>5 where N is the number of lines in the initial complaint(after trying out different bounds on the number of lines like root(N), log(N) etc.) we felt the output for N/2 was better. It uses the NLTK library to do text ranking.
 
 5. The summarized text is then passed to the **Spam Classfier**(which classifies whether the complaint is a spam complaint or not) and the **Complaints Classifier** which classifies the complaint into a category among the 12 different categories we have used.
 
 6. For both the classifiers, a successful call will print a json file and a series of "Not ready yet" messages follow until the output is obtained from AWS.
 
 7. The output is written in a text file named **Outputs.txt** created in the same directory as driver.py
 
 8. The program terminates with the message "Check Outputs.txt".

* The output will be written as a text file "Outputs.txt" in the same folder in the following format for each complaint in order:
  
 SPAM (YES/NO) : NO

 TYPE OF COMPLAINT/QUERY : 
 
 OTHER ASSOCIATED COMPLAINT/QUERY TAGS : 

 SUMMARY OF COMPLAINT/QUERY : 

 Contact Number of the Customer :

 Matching Account No(s) : 

**About the dataset**:
We obtained the training data from here : https://www.kaggle.com/sebastienverpile/consumercomplaintsdata/version/1 . We cleaned the data and reduced the types of complaints to 12. We used just about 10% of this data to train the model and about 1% to test its performance.

The folder dataset contains the dataset used for training the spam and complaint classifiers(each stored separately).

For sample test data we have enclosed four audio files and details of few customers.


