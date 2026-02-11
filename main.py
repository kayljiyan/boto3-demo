import boto3
from typing import Annotated
from fastapi import FastAPI, File, UploadFile

app = FastAPI()
s3 = boto3.client("s3")


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = file.file.read()
    file.file.seek(0)
    try:
        s3.upload_fileobj(file.file, "my-python-boto3-app", file.filename)
    except Exception as e:
        return {"error": str(e)}
    finally:
        file.file.close()
    return {"message": "File has been uploaded"}
