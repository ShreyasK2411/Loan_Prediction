"""
This Module pushes files to s3 bucket
"""
import boto3
from tqdm.notebook import tqdm as tqdm

class UploadToS3:
    def __init__(self,region,bucket_name):
        region = self.region
        bucket_name = self.bucket_name
        location = {'LocationConstraint': self.region}
        self.s3resource=boto3.client('s3',self.region)
        buckets = self.s3resource.list_buckets()
        if self.bucket_name not in buckets:
            self.s3resource.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=location)
    def push(self,file_name):
        object_name = os.path.basename(file_name)
        self.s3resource.upload_file(file_name,bucket_name,object_name)
if __name__ == '__main__':
    bucket_name = input('Enter bucket name: ')
    upload = UploadToS3('ap-south-1',bucket_name)
    dir_name = input('Enter directory path: ')
    
    for file in tqdm(os.listdir(dir_name), dynamic_ncols=True):
        upload.push(file)