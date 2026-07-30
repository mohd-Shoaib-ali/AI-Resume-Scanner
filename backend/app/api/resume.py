from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from pathlib import Path
import shutil
from sqlalchemy.orm import Session

from app.services.parser import extract_text
from app.services.extractor import extract_email, extract_phone, extract_name
from app.core.dependencies import get_db
from app.database import models
from app.schemas.resume import ResumeOut

router = APIRouter(prefix="/resume", tags=["Resume"])

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("/upload", response_model=ResumeOut)
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    allowed_types = [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ]

    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Only PDF and DOCX files are allowed")

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        text = extract_text(str(file_path))
        email = extract_email(text)
        phone = extract_phone(text)
        name = extract_name(text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Resume parsing failed: {str(e)}")

    resume = models.Resume(
        name=name,
        email=email,
        phone=phone,
        file_name=file.filename,
        file_path=str(file_path),
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    return resume

@router.get("/", response_model=list[ResumeOut])
def list_resumes(db: Session = Depends(get_db)):
    return db.query(models.Resume).all()