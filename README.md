
# FastAPI + PostgreSQL Backend Setup

This project is a backend setup built with **FastAPI** and **PostgreSQL**. It includes a modular structure with CRUD operations and connected database tables for users, profiles, subscriptions, and POS modules. A `/ping` route is included to verify the health of the API.

---

## ✅ Features

- Modular FastAPI project structure
- PostgreSQL database connection via SQLAlchemy/SQLModel
- REST API routes for:
  - Users
  - Profiles
  - Subscriptions
  - POS Modules
- `/ping` endpoint for health check
- Seed data using Postman
- Environment variables via `.env`
- Project auto-creates tables on startup

---

## 📁 Project Structure

```
fastapi_backend/
├── app/
│   ├── main.py
│   ├── routes/
│   │   ├── ping.py
│   │   ├── user.py
│   │   ├── profile.py
│   │   ├── subscription.py
│   │   └── pos_module.py
│   ├── models/
│   │   ├── user.py
│   │   ├── profile.py
│   │   ├── subscription.py
│   │   └── pos_module.py
│   ├── schemas/
│   │   ├── user.py
│   │   ├── profile.py
│   │   ├── subscription.py
│   │   └── pos_module.py
│   └── database/
│       └── connection.py
├── .env
├── .env.example
├── README.md
└── requirements.txt
```

---

## ⚙️ Requirements

- Python 3.9+
- PostgreSQL
- pip

---

## 📦 Installation & Setup


1. **Create a virtual environment:**

```bash
python -m venv venv
venv\Scripts\activate  # for Windows
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Create `.env` file:**

Create a `.env` file using the template below:

```
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/fastapi_db
```

Or simply copy the `.env.example` and update your credentials:

```bash
copy .env.example .env
```

4. **Run the FastAPI server:**

```bash
uvicorn app.main:app --reload
```

---

## 🧪 Testing the API in Postman

- Base URL: `http://127.0.0.1:8000`

| Method | Endpoint             | Description             |
|--------|----------------------|-------------------------|
| GET    | `/ping`              | Health check            |
| GET    | `/users`             | Get all users           |
| POST   | `/users`             | Create new user         |
| GET    | `/profiles`          | Get all profiles        |
| POST   | `/profiles`          | Create new profile      |
| GET    | `/subscriptions`     | Get all subscriptions   |
| POST   | `/subscriptions`     | Create new subscription |
| GET    | `/pos-modules`       | Get all POS modules     |
| POST   | `/pos-modules`       | Create new POS module   |

### 🧪 Sample POST Body for Users

```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "is_active": true
}
```

### 🧪 Sample POST Body for Profiles

```json
{
  "user_id": 1,
  "bio": "Backend developer"
}
```

### 🧪 Sample POST Body for Subscriptions

```json
{
  "user_id": 1,
  "plan": "Pro Plan"
}
```

### 🧪 Sample POST Body for POS Modules

```json
{
  "name": "Sales Tracker",
  "is_active": true
}
```

---

## ✅ Success Criteria

- [x] Server runs with FastAPI
- [x] PostgreSQL database connected
- [x] Tables created: users, profiles, subscriptions, pos_modules
- [x] `/ping` route tested via Postman
- [x] Modular structure maintained
- [x] .env.example file included
- [x] This `README.md` with full instructions

---
📌 Created by **Syed Shujaa Hussain**  
📧 web.shujaa10@gmail.com  
🌐 [GitHub Profile](https://github.com/Shujaa396)
