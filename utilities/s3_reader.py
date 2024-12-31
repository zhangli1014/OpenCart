import boto3
import json

def get_data_s3(bucket_name,file_key):
    s3 = boto3.client('s3')
    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        data = response['Body'].read().decode('utf-8')
        return json.loads(data)
    except Exception as e:
        print(f"Failed to load data: {e}")
        return None


if __name__=='__main__':
    print(get_data_s3('opencart-login-testdata','LoginInfo.json'))