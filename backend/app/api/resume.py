from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import shutil
from app.services.parser import extract_text
from app.services.extractor import extract_email, extract_phone, extract_name

router = APIRouter(prefix="/resume", tags=["Resume"])

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
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

    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "path": str(file_path),
        "name": name,
        "email": email,
        "phone": phone,
        "extracted_text_preview": text[:500]
    }

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        text = extract_text(str(file_path))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Text extraction failed: {str(e)}")

    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "path": str(file_path),
        "extracted_text_preview": text[:500]
    }