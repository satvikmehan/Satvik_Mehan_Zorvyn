# 💰 Finance Dashboard Backend

## 📌 Overview

This project is a backend system for managing financial records with role-based access control and analytics.

It supports user authentication, CRUD operations on financial records, and dashboard insights such as total income, expenses, and trends.

---

## 🚀 Tech Stack

* Python
* Django
* Django REST Framework
* SQLite
* JWT Authentication

---

## 🔐 Features

### 👤 User Management

* Signup & Login
* Role-based access (Viewer, Analyst, Admin)

### 💰 Financial Records

* Create, Read, Update, Delete records
* Filter by category, type, date
* Pagination support

### 📊 Dashboard APIs

* Total income
* Total expenses
* Net balance
* Category-wise summary
* Monthly trends

### 🔒 Access Control

* Viewer → read only
* Analyst → read + analytics
* Admin → full access

---

## 🔗 API Endpoints

### Auth

* POST /signup/
* POST /login/

### Records

* GET /records/
* POST /records/
* PUT /records/:id/
* DELETE /records/:id/

### Dashboard

* GET /dashboard/summary/
* GET /dashboard/category/
* GET /dashboard/trends/

---

## ⚙️ Setup Instructions

```bash
git clone <repo>
cd finance-backend

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

---

## 🧠 Key Concepts Implemented

* REST API design
* JWT Authentication
* Role-based access control
* Database relationships
* Aggregation queries
* Pagination & filtering

---

## 📌 Assumptions

* Each user can only access their own records
* Roles define permissions strictly
* SQLite used for simplicity

---

## 🌟 Improvements (Future Scope)

* Deploy to cloud (AWS / Render)
* Add caching (Redis)
* Advanced analytics
* Unit testing

---

## 👨‍💻 Author

Satvik Mehan
