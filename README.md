
---

# 🧑‍💻 Simple Login & Profile Web Application

## 📌 Project Overview

This project is a **simple login and signup web application** built to understand **frontend–backend communication**, **database integration**, and **basic authentication flow** using modern web technologies.

Users can:

* Sign up with personal details
* Log in using username and password
* View their profile details after successful login

> ⚠️ This project does **not** use JWT authentication or logout functionality.
> It is intentionally kept simple for learning purposes.

---

## 🛠️ Tech Stack

### Frontend

* HTML
* CSS
* Vanilla JavaScript

### Backend

* Python
* FastAPI

### Database

* MongoDB (local)

---

## 📁 Project Structure

```
login_app/
│
├── backend/
│   ├── main.py          # FastAPI routes
│   ├── database.py      # MongoDB connection
│   └── requirements.txt
│
├── frontend/
│   ├── login.html
│   ├── signup.html
│   ├── profile.html
│   └── style.css
│
└── README.md
```

---

## ⚙️ Application Flow

1. User opens the **Login page**
2. If the user does not have an account, they click **Sign Up**
3. User registers by providing:

   * Username
   * Password
   * Personal details (name, age, email, phone, address)
4. User logs in with username and password
5. On successful login, the **Profile page** is displayed
6. Profile information is fetched from MongoDB and shown in a readable table layout

---

## 🗄️ Database Structure (MongoDB)

**Database:** `login_app`
**Collection:** `users`

Example document:

```json
{
  "username": "john_doe",
  "password": "12345",
  "firstname": "John",
  "lastname": "Doe",
  "age": 24,
  "email": "john@example.com",
  "phone": "9876543210",
  "address": "Bangalore",
  "photo": "https://via.placeholder.com/150"
}
```

> The `photo` field stores a **default avatar URL**, not an uploaded image.

---

## 🚀 How to Run the Project (Development)

### 1️⃣ Start MongoDB

Make sure MongoDB is running locally:

```bash
sudo systemctl start mongod
```

Verify:

```bash
systemctl status mongod
```

---

### 2️⃣ Backend Setup

```bash
cd login_app
python3 -m venv venv
source venv/bin/activate
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

Swagger API Docs:

```
http://127.0.0.1:8000/docs
```

---

### 3️⃣ Frontend Setup

```bash
cd login_app/frontend
python3 -m http.server 5500
```

Open in browser:

```
http://localhost:5500/login.html
```

> ⚠️ Do NOT open HTML files using `file://`
> Always use an HTTP server.

---

## 🎨 UI Features

* Clean login and signup forms
* Signup and Login buttons placed side-by-side
* Profile page with:

  * Avatar
  * Full name
  * Labeled table layout for user details
* Responsive and readable design

---

## ❌ Limitations (Intentional)

* No JWT authentication
* No logout functionality
* Passwords stored in plain text
* No session management
* No role-based access

These features are intentionally excluded to keep the project beginner-friendly.

---

## 🔮 Future Enhancements

* JWT-based authentication
* Logout functionality
* Password hashing
* Profile image upload
* Edit profile option
* Dockerized deployment

---

## 🎓 Learning Outcomes

* Frontend–backend integration
* Handling HTML form data with FastAPI
* MongoDB CRUD operations
* Understanding authentication flow
* Debugging real-world issues (CORS, blocked requests, data mismatch)

---

## 📄 License

This project is created for **learning and educational purposes**.

---


