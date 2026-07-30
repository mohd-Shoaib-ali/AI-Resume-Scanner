from pydantic import BaseModel

class JobBase(BaseModel):
    title: str
    description: str
    skills: str | None = None

class JobCreate(JobBase):
    pass

class JobOut(JobBase):
    id: int

    class Config:
        from_attributes = True