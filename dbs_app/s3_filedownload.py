# ============================================================================= 
""" Downloads File from S3 Bucket in AWS to Local Storage in """
# =============================================================================

import boto3

def download_file(bucket_name,file_name) :
	print("Initiated process to Download File from S3...")
	s3client = boto3.client("s3")
	s3 = boto3.resource('s3') 
	bucket = s3.Bucket(bucket_name)
	for obj in bucket.objects.all():
	    path_list = obj.key.rsplit('/');
	    filename = path_list[-1]
	    if (filename==file_name) :
	        s3client.download_file(bucket_name, obj.key, file_name)
	print("\n")
     
# =============================================================================
