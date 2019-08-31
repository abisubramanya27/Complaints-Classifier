# =============================================================================
# import boto3
# s3 = boto3.resource('s3')
# s3.Bucket('complaintsoutput').download_file('arn:aws:kms:ap-southeast-1:729128127076:key/d416a28c-ca71-4152-8075-67c50fea9172', 'C:\\Users\\HP\\Documents\\random stuff sem III\\vetti.csv')
# 
# =============================================================================

# =============================================================================
import boto3
s3client = boto3.client("s3")
s3 = boto3.resource('s3') 
bucket_name = 'complaintsoutput'
bucket = s3.Bucket(bucket_name)
for obj in bucket.objects.all():
    filename = obj.key.rsplit('/')[-1]
    #if filename=='output.tar.gz':
    s3client.download_file(bucket_name, obj.key, "C:\\Users\\HP\\Desktop" + filename)
# 
# =============================================================================
