# 💰 Finance Dashboard Backend (Django + DRF)

## 📌 Overview

This project is a backend system for a finance dashboard that allows users to manage financial records, view analytics, and interact with data based on their roles.

It is built using **Django** and **Django REST Framework**, with a focus on clean architecture, role-based access control, and scalable API design.

---

## 🚀 Features

### 👤 User & Role Management

* User registration (default role: **viewer**)
* Role-based access control:

  * **Viewer** → Read-only access
  * **Analyst** → Read + analytics access
  * **Admin** → Full CRUD access

---

### 💵 Financial Records Management

* Create, read, update, delete records
* Fields:

  * Amount
  * Type (income / expense)
  * Category
  * Date
  * Notes
* Filtering support:

  * By type
  * By category
  * By date

---

### 📊 Dashboard APIs

* Total income
* Total expenses
* Net balance
* Category-wise breakdown
* Monthly trends

---

### 🔐 Authentication & Security

* JWT-based authentication
* Protected APIs using token
* Role-based permissions
* Secure password hashing

---

### ⚙️ Additional Features

* Pagination for records
* Service layer for business logic
* Clean error handling
* Structured API responses

---

## 🏗️ Tech Stack

* **Backend**: Django, Django REST Framework
* **Database**: SQLite
* **Authentication**: JWT (SimpleJWT)

---

## 📂 Project Structure

```
finance-dashboard/
│
├── users/        # user model, auth, permissions
├── records/      # financial records APIs
├── dashboard/    # analytics & summary APIs
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚡ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd finance-dashboard
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Create Admin User

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Run Server

```bash
python manage.py runserver
```

---

## 🔑 Authentication Flow

### Signup

```
POST /signup/
```

### Login (Get Token)

```
POST /api/token/
```

### Use Token

```
Authorization: Bearer <access_token>
```

---

## 📡 API Endpoints

| Endpoint               | Method         | Description         |
| ---------------------- | -------------- | ------------------- |
| `/signup/`             | POST           | Register user       |
| `/api/token/`          | POST           | Login (JWT)         |
| `/records/`            | GET/POST       | List/Create records |
| `/records/<id>/`       | GET/PUT/DELETE | Record details      |
| `/dashboard/summary/`  | GET            | Overall summary     |
| `/dashboard/category/` | GET            | Category breakdown  |
| `/dashboard/trends/`   | GET            | Monthly trends      |

---

## 🛡️ Access Control

| Role    | Permissions      |
| ------- | ---------------- |
| Viewer  | Read-only        |
| Analyst | Read + dashboard |
| Admin   | Full access      |

---

## 🧪 Testing

The APIs were tested using **Thunder Client**.

Test scenarios include:

* Authentication (valid/invalid token)
* Role-based restrictions
* CRUD operations
* Filtering and pagination
* Dashboard analytics

---

## 🧠 Design Decisions

* Used **service layer** to separate business logic from views
* Implemented **custom permissions** for role-based access
* Default role set to **viewer** to prevent privilege escalation
* Structured responses for consistency

---

## 📌 Conclusion

This project demonstrates:

* Clean backend architecture
* Secure authentication & authorization
* Proper API design
* Real-world backend development practices

---

## 👨‍💻 Author

Satvik Mehan
