from pydantic import BaseModel

class ResumeBase(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    file_name: str
    file_path: str

class ResumeCreate(ResumeBase):
    pass

class ResumeOut(ResumeBase):
    id: int

    class Config:
        from_attributes = True