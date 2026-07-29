from fastapi import FastAPI
from app.database.database import engine, Base
from app.database import models
from app.api.resume import router as resume_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Resume Screening Platform",
    description="Backend API for resume screening and ranking",
    version="1.0.0"
)

app.include_router(resume_router)

@app.get("/")
def root():
    return {"message": "AI Resume Screening Platform is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

