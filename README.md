# 🚀 Job Services Master API

A layered FastAPI application for managing job records using PostgreSQL and SQLAlchemy.

This project follows an industry-standard **Layered Architecture Pattern**:
Controller → Service → Repository → Model → Database

---

## 📌 Tech Stack

- **Backend Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Database:** PostgreSQL
- **Data Validation:** Pydantic
- **ASGI Server:** Uvicorn
- **Language:** Python 3.10+

---

## 🏗 Architecture Overview

This application follows a clean separation of concerns:

```
Client
  ↓
Controller (API Routes)
  ↓
Service Layer (Business Logic)
  ↓
Repository Layer (Database Access)
  ↓
PostgreSQL Database
```

Each layer has a single responsibility.

---

## 📂 Project Structure

```
JobProject/
│
├── JobControllerMaster/
│   └── job_controller_master.py
│
├── JobServicesMaster/
│   └── job_services_master.py
│
├── JobServiceImplementation/
│   └── job_service_implementation_master.py
│
├── JobRepositoryDAO/
│   └── repository_DAO.py
│
├── JobModdelEntityMaster/
│   └── model_entity_master_table.py
│
├── JobRequestResponseMaster/
│   └── job_request_response_master.py
│
├── JobDatabaseConnection/
│   └── database_connection_job.py
│
└── main.py
```

---

## 🗄 Database Schema

### Table: `job_table`

| Column Name      | Type      | Description |
|------------------|-----------|------------|
| job_id           | Integer   | Primary Key |
| job_code         | String    | Unique Job Code |
| job_name         | String    | Job Title |
| job_company      | String    | Company Name |
| job_date_post    | DateTime  | Job Posted Date |
| job_applied      | String    | Application Status |
| job_country      | String    | Job Location |
| job_email        | String    | Applicant Email (Unique) |
| job_date_apply   | String    | Date Applied |

---

## 📦 Features

- ✅ Create Job Record
- ✅ Fetch All Jobs
- ✅ Fetch Job by Code & Email
- ✅ Update Job
- ✅ Delete Job
- ✅ Layered Architecture
- ✅ Dependency Injection
- ✅ SQLAlchemy ORM Mapping
- ✅ Pydantic Validation

---

## 🔌 API Endpoints

### 🔹 Create Job

**POST** `/create_job`

Request Body:
```json
{
  "job_code": "J101",
  "job_name": "Data Scientist",
  "job_company": "ABC Corp",
  "job_date_post": "2025-02-01T10:00:00",
  "job_applied": "Yes",
  "job_country": "India",
  "job_email": "example@gmail.com",
  "job_date_apply": "2025-02-05"
}
```

---

### 🔹 Get All Jobs

**GET** `/get_jobs`

---

### 🔹 Get Job by Code & Email

**GET** `/get`

Query Parameters:
```
job_code=J101
job_email=example@gmail.com
```

---

### 🔹 Update Job

**PUT** `/update_job`

---

### 🔹 Delete Job

**DELETE** `/delete_job`

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd JobProject
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🛢 Database Configuration

Update your database connection in:

```
JobDatabaseConnection/database_connection_job.py
```

Example:

```python
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "job_master"
DB_USER = "postgres"
DB_PASSWORD = "your_password"
```

Make sure PostgreSQL is running.

---

## ▶️ Running the Application

```bash
python main.py
```

Or directly:

```bash
uvicorn JobControllerMaster.job_controller_master:app --reload
```

Application runs at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## 🧠 Design Principles Used

- Separation of Concerns
- Dependency Injection
- Interface-based Service Layer
- ORM Abstraction
- Input Validation
- Clean Code Structure

---

## 🚨 Known Improvements (Future Enhancements)

- Add JWT Authentication
- Add Logging
- Add Global Exception Handling
- Use Alembic for migrations
- Dockerize the application
- Add Unit & Integration Tests
- Implement Pagination
- Add Environment Variable Configuration (.env)

---

## 📈 Future Enhancements

- Convert to Microservice Architecture
- Add Role-Based Access Control
- Implement CI/CD Pipeline
- Deploy to AWS / Azure / GCP
- Add Caching Layer (Redis)

---

## 👨‍💻 Author

**Sujit Maity**

---

## 📜 License

This project is for learning and demonstration purposes.
