
# 🧾 FastAPI Admin Backend Panel

A backend admin panel built with **FastAPI** and **PostgreSQL**, designed to manage users, profiles, subscriptions, and POS modules.

---

## 🛠️ Tech Stack
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-FF0000?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-000000?style=for-the-badge&logo=python&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

---

## 📖 Overview

This project is an admin backend system for managing platform modules, built using FastAPI and PostgreSQL. It supports:

- 👤 User management
- 🧾 Profiles management
- 💳 Subscriptions
- 🧩 POS Modules

---

## ✨ Features

- ✅ Modular route structure
- ✅ CRUD operations for Users, Profiles, Subscriptions, and POS Modules
- ✅ `/ping` health check route
- ✅ PostgreSQL DB connection with SQLAlchemy/SQLModel
- ✅ REST API tested with Postman
- ✅ Seed data insertion supported

---

## 📁 Folder Structure

```
fastapi_backend/
├── app/
│   ├── routes/
│   ├── models/
│   ├── schemas/
│   ├── database/
│   └── main.py
├── venv/
├── .env
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Setup Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
# source venv/bin/activate  # On Linux/Mac
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Create a `.env` file:

```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fastapi_db
```

### 5. Run the App

```bash
uvicorn app.main:app --reload
```

---

## 🧪 API Testing (Postman)

| Endpoint              | Method | Description         |
|-----------------------|--------|---------------------|
| `/ping`              | GET    | Health check        |
| `/users`             | GET/POST | Manage users     |
| `/profiles`          | GET/POST | Manage profiles   |
| `/subscriptions`     | GET/POST | Manage subscriptions |
| `/posmodules`        | GET/POST | Manage POS modules |

> For POST requests, pass JSON body in raw format.

---

## ✅ Project Checklist

- [x] FastAPI project runs on localhost
- [x] PostgreSQL connected and tables created
- [x] Routes for all models tested via Postman
- [x] Modular structure maintained
- [x] `.env.example` created

---

## 👨‍💻 Author

**Syed Shujaa Hussain**

[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:web.shujaa10@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Shujaa396)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/syed-shujaa-hussain-69113b289)

---

## 🏁 Final Notes

✅ Fully working admin backend system built with FastAPI + PostgreSQL  
✅ Designed for modularity, simplicity, and testing convenience  
