from sqlalchemy.orm import Session
from pydantic import EmailStr
from JobModdelEntityMaster.model_entity_master_table import ModelEntityMaster
from JobRequestResponseMaster.job_request_response_master import ( UpdateJobRequestMaster, JobRequestCodeEmail,
                                                                  DeleteJobRequestMaster, JobResponseMaster)

class RepositoryDAOMaster:

    def display_all_jobs_from_database(self, database: Session):
        return database.query(ModelEntityMaster).all()

    def create_job_request(self, database: Session, create_request: ModelEntityMaster):
        database.add(create_request)
        database.commit()
        database.refresh(create_request)
        return create_request

    def delete_job_request(self, database: Session, delete_request: DeleteJobRequestMaster):
        delete_data = database.query(ModelEntityMaster).filter(
            ModelEntityMaster.job_code == delete_request.job_code,
            ModelEntityMaster.job_email == delete_request.job_email
        ).first()

        if not delete_data:
            return {
                'STATUS': 'JOB DOES NOT EXIST',
            }
        database.delete(delete_data)
        database.commit()
        return {
            'STATUS': 'SUCCESS',
            'MESSAGE': 'Job deleted successfully',
        }

    def update_job_request(self, database: Session, update_request: UpdateJobRequestMaster):
        update_data = database.query(ModelEntityMaster).filter(
            ModelEntityMaster.job_code == update_request.job_code,
            ModelEntityMaster.job_email == update_request.job_email
        ).first()

        if not update_data:
            return {
                "message": "Job request not found"
            }

        update_data_to_storage = update_request.dict(
            exclude_unset=True
        )

        update_data_to_storage.pop("job_code", None)
        update_data_to_storage.pop("job_email", None)

        for key, value in update_data_to_storage.items():
            setattr(update_data, key, value)

        database.commit()
        database.refresh(update_data)
        return {
            "message": "Job request updated",
            'STATUS': update_data
        }

    def fetch_all_jobs_from_database_code_email(self, database: Session, request: JobRequestCodeEmail):
        return database.query(ModelEntityMaster).filter(
            ModelEntityMaster.job_code == request.job_code,
            ModelEntityMaster.job_email == request.job_email
        ).first()
