# Complaints-Classifier
A complaints classifer for banks built using Python and Amazon Web Services(AWS)

Instructions for use:
* Run : `pip install -r requirements.txt` in Shell to Download all Necessary Packages for running the Application
* Install and Set Up [AWS CLI](https://aws.amazon.com/cli/)
* Configure it with:
`aws configure`
using the access key provided.

* **Setting up the inputs:**

  * The input audio file(which is the complaint) should be stored as "test-audio.mp3".
  
  * The relevant contact numbers of the customers should be stored in the csv file in ./Database/Accno_Phno_db.csv (we have added some sample contact number + account number in it).
  
* The output will be written as a text file "output.txt" in the same folder in the following format:
  
  SPAM (YES/NO) :
  
  TYPE OF COMPLAINT :
  
  SUMMARY OF COMPLAINT :
  
  Contact Number of the Complainant :
  
  Matching Account No(s) :
  
  ORIGINAL COMPLAINT :

The folder dataset contains the dataset used for training the spam and complaint classifiers(each stored separately).
