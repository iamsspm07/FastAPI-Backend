from sqlalchemy.orm import Session
from typing import List
from fastapi import FastAPI, Depends, status


from JobDatabaseConnection.database_connection_job import *
from JobRequestResponseMaster.job_request_response_master import *
from JobServiceImplementation.job_service_implementation_master import JobServicesFunctionMasterImplementation

app = FastAPI(title="Job Services Master API", version="1.0")

BASE.metadata.create_all(bind=ENGINE)

serviceImplementation = JobServicesFunctionMasterImplementation()

@app.post('/create_job', response_model=JobResponseMaster, status_code=status.HTTP_201_CREATED)
def create_job(job_create: CreateJobRequestMaster, database: Session = Depends(database_connection)):
    return serviceImplementation.create_function_job(database, job_create)

@app.get('/get_jobs', response_model=List[JobResponseMaster])
def get_jobs(database: Session = Depends(database_connection)):
    return serviceImplementation.display_function_job(database)

@app.delete('/delete_job')
def delete_function_job(delete_job_request: DeleteJobRequestMaster, database: Session = Depends(database_connection)):
    return serviceImplementation.delete_function_job(database, delete_job_request)

@app.put('/update_job')
def update_function(update: UpdateJobRequestMaster, database: Session = Depends(database_connection)):
    return serviceImplementation.update_function_job(database, update)

@app.get('/get', response_model=List[JobResponseMaster])
def get_jobs(param: JobRequestCodeEmail, database: Session = Depends(database_connection)):
    return serviceImplementation.display_function_job_code_email(database, param)

@app.get('/')
def read_root():
    return {'Hello': 'World'}