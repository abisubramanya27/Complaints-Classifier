# ============================================================================= 
""" Uploads File from Local Storage to S3 Bucket in AWS  """
# =============================================================================

import boto3

def upload(path, bucket_name, filename) :

	print("Initiated Uploading Files to S3...")

	# Create an S3 client
	s3 = boto3.client('s3')

	# Uploads the given file using a managed uploader, which will split up large
	# files automatically and upload parts in parallel.
	s3.upload_file(path+filename, bucket_name, filename)
	print("\n")

# =============================================================================