from fastapi import FastAPI
from app.api.upload import router as upload_router

app = FastAPI(
    title="CourtProof API",
    version="1.0",
    description="AI-powered Deepfake Detection Platform"
)

app.include_router(upload_router)


@app.get("/")
def home():
    return {
        "project": "CourtProof",
        "status": "Backend Running Successfully"
    }