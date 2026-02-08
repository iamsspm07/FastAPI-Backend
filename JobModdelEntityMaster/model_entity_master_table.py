from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from JobDatabaseConnection.database_connection_job import BASE

class ModelEntityMaster(BASE):
    __tablename__ = 'job_table'

    job_id = Column(Integer, primary_key=True, index=True)
    job_code = Column(String, nullable=False, unique=True)
    job_name = Column(String, nullable=False)
    job_company = Column(String, nullable=False)
    job_date_post =Column(DateTime, default=datetime.utcnow)
    job_applied = Column(String, nullable=False)
    job_country = Column(String, nullable=False)
    job_email = Column(String, nullable=False, unique=True)
    job_date_apply = Column(String, nullable=False)