# ==========================================================================================
""" Creates Training Model for AWS Comprehend from Data in S3 Bucket  """
# ==========================================================================================

import boto3

# Instantiate Boto3 SDK:
client = boto3.client('comprehend','ap-southeast-1')

# Create a document classifier
create_response = client.create_document_classifier(
    InputDataConfig={
        'S3Uri': 's3://bankcomplaints/complaint_train.csv'
    },
    DataAccessRoleArn='arn:aws:iam::729128127076:role/pshift',
    DocumentClassifierName='Complaintclassifierv1',
    LanguageCode='en'
)
print("Create response: %s\n", create_response)

# Check the status of the classifier
describe_response = client.describe_document_classifier(
    DocumentClassifierArn=create_response['DocumentClassifierArn'])
print("Describe response: %s\n", describe_response)

# List all classifiers in account
list_response = client.list_document_classifiers()
print("List response: %s\n", list_response)

# ==========================================================================================



