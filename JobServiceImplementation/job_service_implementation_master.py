from sqlalchemy.orm import Session
from JobModdelEntityMaster.model_entity_master_table import ModelEntityMaster
from JobRequestResponseMaster.job_request_response_master import *
from JobServicesMaster.job_services_master import JobServicesFunctionMaster
from JobRepositoryDAO.repository_DAO import *

class JobServicesFunctionMasterImplementation(JobServicesFunctionMaster):

    def __init__(self):
        self.repository_dao = RepositoryDAOMaster()

    def create_function_job(self, database: Session, create_job_request: CreateJobRequestMaster):
        create = ModelEntityMaster(**create_job_request.model_dump())
        return self.repository_dao.create_job_request(database, create)

    def delete_function_job(self, database: Session, delete_job_request: DeleteJobRequestMaster):
        return self.repository_dao.delete_job_request(database, delete_job_request)

    def update_function_job(self, database: Session, update_job_request: UpdateJobRequestMaster):
        return self.repository_dao.update_job_request(database, update_job_request)

    def display_function_job(self, database: Session):
        return self.repository_dao.display_all_jobs_from_database(database)

    def display_function_job_code_email(self, database: Session, display_request: JobRequestCodeEmail):
        return self.display_function_job_code_email(database, display_request)