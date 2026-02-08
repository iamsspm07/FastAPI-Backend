from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional
from datetime import datetime


# REQUEST:
class CreateJobRequestMaster(BaseModel):
    job_code: str
    job_name: str
    job_company: str
    job_date_post: Optional[datetime]
    job_applied: str
    job_country: str
    job_email: EmailStr
    job_date_apply: str

class UpdateJobRequestMaster(BaseModel):
    job_code: str
    job_name: Optional[str]
    job_company: Optional[str]
    job_date_post: Optional[datetime]
    job_applied: Optional[str]
    job_country: Optional[str]
    job_email: EmailStr
    job_date_apply: Optional[str]

class DeleteJobRequestMaster(BaseModel):
    job_code: str
    job_email: EmailStr

class JobRequestCodeEmail(BaseModel):
    job_code: str
    job_email: EmailStr

# RESPONSE:
class JobResponseMaster(BaseModel):
    job_id: int
    job_code: str
    job_name: str
    job_company: str
    job_date_post: Optional[datetime]
    job_applied: str
    job_country: str
    job_email: EmailStr
    job_date_apply: str

    model_config = ConfigDict(from_attributes=True)
