import boto3, os
from fastapi import FastAPI, File, UploadFile
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

app = FastAPI()
s3 = boto3.client(
    service_name="s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


@app.get("/")
def home():
    return {
        "message": "Hello World! This is the home page of the API. Please visit /docs to see the API documentation."
    }


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = file.file.read()
    file.file.seek(0)
    try:
        s3.upload_fileobj(file.file, S3_BUCKET_NAME, file.filename)
    except Exception as e:
        return {"error": str(e)}
    finally:
        file.file.close()
    return {"message": "File has been uploaded"}
