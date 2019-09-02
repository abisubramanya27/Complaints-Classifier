# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:26:31 2019

@author: ANISWAR
"""

from __future__ import print_function
import time
import boto3
import random
import string
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
transcribe = boto3.client('transcribe')
job_name = randomString(10)
job_uri = "s3://audio-complaint/transcribe-sample.mp3"
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