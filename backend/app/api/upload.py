from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import shutil
import uuid

router = APIRouter()

UPLOAD_DIR = "../uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_TYPES = {
    "image/jpeg",
    "image/png",
    "image/webp",
    "video/mp4",
    "video/quicktime",
    "video/x-msvideo"
}

MAX_FILE_SIZE = 100 * 1024 * 1024  # 100 MB


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only image and video files are allowed."
        )

    unique_name = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, unique_name)

    content = await file.read()

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File exceeds maximum size."
        )

    with open(file_path, "wb") as buffer:
        buffer.write(content)

    return {
        "filename": unique_name,
        "content_type": file.content_type,
        "size_bytes": len(content),
        "message": "Upload successful"
    }