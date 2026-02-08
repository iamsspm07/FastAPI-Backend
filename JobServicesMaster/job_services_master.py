from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from JobRequestResponseMaster.job_request_response_master import CreateJobRequestMaster, DeleteJobRequestMaster, \
    UpdateJobRequestMaster, JobRequestCodeEmail


class JobServicesFunctionMaster(ABC):

    @abstractmethod
    def create_function_job(self, database: Session, create_job_request: CreateJobRequestMaster):
        pass

    @abstractmethod
    def delete_function_job(self, database: Session, delete_job_request: DeleteJobRequestMaster):
        pass

    @abstractmethod
    def update_function_job(self, database: Session, update_job_request: UpdateJobRequestMaster):
        pass

    @abstractmethod
    def display_function_job(self, database: Session):
        pass

    @abstractmethod
    def display_function_job_code_email(self, database: Session, display_request: JobRequestCodeEmail):
        pass