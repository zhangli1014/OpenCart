import boto3
import os
import shutil
from utilities.readconfig import readConfig
import datetime
def upload_report_to_s3(local_dir, bucket_name, s3_folder):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Upload each file in the report directory
    for root, dirs, files in os.walk(local_dir):
        for file in files:
            # Create the S3 path
            s3_path = os.path.join(s3_folder, os.path.relpath(os.path.join(root, file), local_dir))
            try:
                s3.upload_file(os.path.join(root, file), bucket_name, s3_path)
                print(f"Successfully uploaded {file} to {bucket_name}/{s3_path}")
            except Exception as e:
                print(f"Error uploading {file}: {e}")

bucket_name = readConfig.getconfig('s3 info', 'bucketName')
today = datetime.datetime.now().strftime("%Y-%m-%d")
# Example usage:
upload_report_to_s3('./allure-report', bucket_name, today)
