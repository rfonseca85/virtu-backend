from pydantic import BaseModel


class CoverLetter(BaseModel):
    coverLetter: str


class CoverLetterRequest(BaseModel):
    companyName: str
    jobTitle: str
    jobDescription: str








