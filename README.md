🚀 Admin Panel Backend – FastAPI + PostgreSQL

Backend system for an Admin Panel built using FastAPI and PostgreSQL, providing modular APIs for managing users, profiles, subscriptions, and POS modules.

🛠️ Tech Stack







📖 Overview

This project includes:

🔐 JWT-based authentication structure

🧍 Users can be created, listed

📄 Profiles assigned to users

💳 Subscription system

🖥️ POS Modules CRUD support

🩺 /ping endpoint for API health check

📦 Modular and scalable folder structure

📁 Folder Structure

fastapi_backend/
├── app/
│   ├── routes/           # 🔁 API route files
│   ├── models/           # 🧱 ORM models
│   ├── schemas/          # 📦 Pydantic schemas
│   └── database/         # 🗄️ DB connection + session
├── main.py               # 🚦 FastAPI entry point
├── .env                  # 🔐 Environment variables
└── .env.example          # 📄 Sample .env file

✨ Features

✅ Users CRUD

✅ Profiles associated with users

✅ Subscriptions management

✅ POS Modules for system features

✅ PostgreSQL DB with SQLModel/SQLAlchemy

✅ Modular FastAPI routes and schemas

✅ Tested with Postman

📦 Setup Instructions

1. Clone Repository

git clone https://github.com/your-username/admin-panel-backend.git
cd admin-panel-backend

2. Create Virtual Environment

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Install Requirements

pip install -r requirements.txt

4. Configure .env

DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fastapi_db

5. Run Server

uvicorn app.main:app --reload

🔐 API Endpoints

Route

Method

Description

/ping

GET

API Health Check

/users

GET

List all users

/users

POST

Create a user

/profiles

GET

List all profiles

/profiles

POST

Create a profile

/subscriptions

GET

List all subscriptions

/subscriptions

POST

Create a subscription

/pos-modules

GET

List all POS modules

/pos-modules

POST

Create a POS module

Use Postman to test these routes with http://127.0.0.1:8000

🧪 API Testing via Postman

✅ Create and get users

✅ Create and get profiles

✅ Create and get subscriptions

✅ Create and get POS modules

✅ Check server with /ping

📷 Suggested Screenshots for Submission

Postman testing all routes (GET & POST)

PgAdmin showing database tables

Successful server terminal output

GitHub repo overview with README

✅ Milestone Checklist

Milestone

Status

FastAPI Server Runs

✅

Connected to PostgreSQL

✅

Created Tables: Users, Profiles, Modules

✅

/ping tested with Postman

✅

.env.example added

✅

README with setup instructions

✅

Seed data inserted and verified

✅

Project pushed to GitHub

✅

🧾 Final Notes

🧩 All components modular and reusable

⚙️ Admin/User routes structured clearly

📂 Code is production-ready and documented

👤 Author

Syed Shujaa Hussain





🏁 Success Criteria

✅ All UIs functional and responsive✅ Backend setup and connected with DB✅ Codebase synced with GitHub✅ Modular components✅ Admin/User flows separated

