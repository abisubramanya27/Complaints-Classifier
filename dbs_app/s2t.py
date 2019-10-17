# ==========================================================================================
""" Converts Audio File in S3 Bucket to Text and stores in S3 Bucket in AWS  """
# ==========================================================================================

from __future__ import print_function
import time
import boto3
import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def s2t(filepath) :
    print("Initiated Speech To Text...")
    transcribe = boto3.client('transcribe')
    job_name = randomString(10)
    job_uri = "s3://"+filepath
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='mp3',
        LanguageCode='en-US',
        OutputBucketName='audio-complaint'
    )
    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        print("Not ready yet...")
        time.sleep(60)
    print(status)
    print("\n")
    return job_name

# ============================================================================================