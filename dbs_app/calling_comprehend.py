# ======================================================================================================== 
""" Calls the Trained Classification Models in AWS Comprehend to extract Labels to S3 Bucket in AWS """
# ========================================================================================================

from __future__ import print_function
import time
import boto3


def comprehend(S3_extension,training_model,output_path) :

    print("Initiated Calling Comprehend to use the trained Model...")

    #Instantiate Boto3 SDK:
    client = boto3.client('comprehend', region_name='ap-southeast-1')

    start_response = client.start_document_classification_job(
        InputDataConfig={
            'S3Uri': 's3://'+S3_extension,
            'InputFormat': 'ONE_DOC_PER_LINE'
        },
        OutputDataConfig={
            'S3Uri': 's3://'+output_path
        },
        DataAccessRoleArn='arn:aws:iam::729128127076:role/pshift',
        DocumentClassifierArn=
        'arn:aws:comprehend:ap-southeast-1:729128127076:document-classifier/'+training_model
    )

    print("Start response: %s\n", start_response)
    JobID=start_response['JobId']

    #Check the status of the job
    describe_response = client.describe_document_classification_job(JobId=start_response['JobId'])
    print("Describe response: %s\n", describe_response)

    #List all classification jobs in account
    list_response = client.list_document_classification_jobs()
    print("List response: %s\n", list_response)

    while True:
        status = client.describe_document_classification_job(
        JobId = JobID
    )
        if status['DocumentClassificationJobProperties']['JobStatus'] == 'COMPLETED':
            break
        elif status['DocumentClassificationJobProperties']['JobStatus'] == 'FAILED':
            print("FAILED!!")
        print("Not ready yet...")
        time.sleep(30)

    print(status)
    print("\n")

# ========================================================================================================
