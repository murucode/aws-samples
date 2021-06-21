import boto3
import os
import sys
import uuid

def lambda_handler(event, context):
    
    bucket_name = "bucket Name"
    
    s3_client = boto3.client('s3')
    
    download_path = '/tmp/{}{}'.format(uuid.uuid4(), 'test.txt')
    print(download_path)
    
    # Download the file from S3
    s3_client.download_file(bucket_name, 'Hello.txt',download_path)
    print(open(download_path).read())
