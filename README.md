# 🚀 Job Services Master API

A structured and scalable **FastAPI-based REST API** for managing job applications.

This project follows a clean multi-layered architecture using:

- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic Validation
- Repository–Service–Controller Pattern

---

## 📌 Project Overview

This API allows users to:

- ✅ Create job applications
- ✅ Fetch all job records
- ✅ Fetch job by `job_code` & `job_email`
- ✅ Update job details
- ✅ Delete job entries

The architecture ensures:

- Clean separation of concerns  
- Maintainable codebase  
- Scalable backend structure  
- Easy testing and extensibility  

---

## 🏗 Architecture Design
Controller Layer (FastAPI Routes)
↓
Service Layer (Business Logic)
↓
Repository Layer (DAO)
↓
PostgreSQL Database


---

## 🛠 Tech Stack

| Technology   | Purpose            |
|--------------|-------------------|
| FastAPI      | Web Framework      |
| PostgreSQL   | Database           |
| SQLAlchemy   | ORM                |
| Pydantic     | Data Validation    |
| Uvicorn      | ASGI Server        |

---

## 📂 Project Structure

```
JobServicesMaster/
│
├── JobControllerMaster/
│   └── job_controller_master.py
│
├── JobDatabaseConnection/
│   └── database_connection_job.py
│
├── JobModdelEntityMaster/
│   └── model_entity_master_table.py
│
├── JobRepositoryDAO/
│   └── repository_DAO.py
│
├── JobRequestResponseMaster/
│   └── job_request_response_master.py
│
├── JobServiceImplementation/
│   └── job_service_implementation_master.py
│
├── JobServicesMaster/
│   └── job_services_master.py
│
└── main.py
```

---

# Clone Repository:

git clone https://github.com/your-username/job-services-master.git
cd job-services-master

# Create Virtual Environment:

python -m venv venv
venv\Scripts\activate
OR
python3 -m venv venv
source venv/bin/activate
