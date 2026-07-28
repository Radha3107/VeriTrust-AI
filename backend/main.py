from fastapi import FastAPI, UploadFile, File
import os
import shutil

app = FastAPI(
    title="CourtProof API",
    description="AI-Powered Deepfake Detection Platform",
    version="1.0"
)

UPLOAD_DIR = "../uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def home():
    return {
        "project": "CourtProof",
        "status": "Backend Running Successfully"
    }


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "File uploaded successfully!"
    }