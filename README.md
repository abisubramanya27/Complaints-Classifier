# Complaints-Classifier
A complaints classifer for banks built using Python and Amazon Web Services(AWS)

Instructions for use:
* Run : `pip install -r requirements.txt` in Shell to Download all Necessary Packages for running the Application
* Install and Set Up [AWS CLI](https://aws.amazon.com/cli/)
* Configure it with:
`aws configure`
using the access key ID and the secret access key provided in the csv file **rootkeysubmission.csv**. The user ID we have provided have the permission to run Amazon Comprehend, Amazon Transcribe and as well as read/write in our S3 bucket.

* **Setting up the inputs:**

  * The input audio file(which is the complaint) should be stored as "test-audio<number>.mp3" and they will be classified in the same order.
  * The relevant contact numbers of the customers along with their account numbers should be stored in the csv file in ./Database/Accno_Phno_db.csv (we have added some sample contact number + account number in it).

* **Running the program**
 
 1. Run the python file **driver.py** for each audio file it takes approximately 10 minutes to finish running(includeing the time taken by the classifiers).
 
 2. First the given audio is converted into text file using amazon transcribe. A successful call to transcribe will print a json file. Importantly the json file contains the job id **AND CRAP**.
 
 3. This is followed by a series of "Not Ready Yet" messages every 30 seconds till the output is received from AWS. The output is taken from the S3 bucket and is downloaded locally and stored as string variable(s).
 
 4. This text is then passed to the summarization function which summarizes the text in √ N lines where N is the number of lines in the initial complaint. It uses the NLTK library to do text ranking.
 
 5. The summarized text is then passed to the **Spam Classfier**(which classifies whether the complaint is a spam complaint or not) and the **Complaints Classifier** which classifies the complaint into a category among the 12 different categories we have used.
 
 6. For both the classifier after they are called, a successful call to transcribe will print a json file(which will be printed in the terminal) and a series of "Not ready yet" messages follow until the output is obtained from AWS.
 
 7. The output is written in a text file named **outputs.txt** created in the same directory as driver.py
 
 8. The program terminates with the message "Check outputs.txt".

* The output will be written as a text file "output.txt" in the same folder in the following format:
  
  SPAM (YES/NO) :
  
  TYPE OF COMPLAINT :
  
  SUMMARY OF COMPLAINT :
  
  Contact Number of the Complainant :
  
  Matching Account No(s) :
  
  ORIGINAL COMPLAINT :

The folder dataset contains the dataset used for training the spam and complaint classifiers(each stored separately).
