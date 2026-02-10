import boto3

s3 = boto3.client('s3')

file = input("Enter file name: ")
try:
    s3.upload_file(file, "my-python-boto3-app", file)
except Exception as e:
    print(str(e))
