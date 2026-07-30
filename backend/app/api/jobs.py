from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.database import models
from app.schemas.job import JobCreate, JobOut

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/", response_model=JobOut)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    job_obj = models.Job(
        title=job.title,
        description=job.description,
        skills=job.skills,
    )
    db.add(job_obj)
    db.commit()
    db.refresh(job_obj)
    return job_obj

@router.get("/", response_model=list[JobOut])
def list_jobs(db: Session = Depends(get_db)):
    return db.query(models.Job).all()