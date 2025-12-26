
---

# 🧑‍💻 Login & Profile Web Application (Dockerized)

## 📌 Project Overview

This project is a **simple login and profile web application** built to understand **frontend–backend communication**, **database integration**, and **basic authentication flow**, using a **containerized, industry-style setup**.

The application is fully **Dockerized using Docker Compose**, enabling consistent execution across environments without manual local configuration.

Users can:

* Sign up with personal details
* Log in using username and password
* View their profile details after successful login

> ⚠️ This project intentionally avoids JWT authentication and logout functionality to keep the focus on **core backend logic and infrastructure fundamentals**.

---

## 🛠️ Tech Stack

### Frontend

* HTML
* CSS
* Vanilla JavaScript
* Nginx (for serving static files)

### Backend

* Python
* FastAPI

### Database

* MongoDB

### DevOps / Infrastructure

* Docker
* Docker Compose

---

## 📁 Project Structure

```
user-profile-pro/
│
├── backend/
│   ├── main.py              # FastAPI routes
│   ├── database.py          # MongoDB connection logic
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── index.html           # Login page (entry point)
│   ├── signup.html
│   ├── profile.html
│   ├── style.css
│   └── Dockerfile
│
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## ⚙️ Application Flow

1. User opens the **Login page**
2. If the user does not have an account, they navigate to **Sign Up**
3. User registers by providing:

   * Username
   * Password
   * Personal details (name, age, email, phone, address)
4. User logs in using username and password
5. On successful login, the **Profile page** is displayed
6. Profile information is fetched from MongoDB and rendered in a readable layout

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

## 🚀 Running the Project (Docker – Recommended)

### 1️⃣ Prerequisites

* Docker
* Docker Compose

Verify installation:

```bash
docker --version
docker compose version
```

---

### 2️⃣ Environment Configuration

Create a `.env` file in the project root:

```env
MONGO_USERNAME=admin
MONGO_PASSWORD=secret
```

> ⚠️ Do **NOT** commit `.env` to GitHub
> Use `.env.example` as a reference.

---

### 3️⃣ Start the Application

```bash
docker compose down -v
docker compose up --build
```

This command:

* Builds backend and frontend images
* Starts MongoDB with authentication
* Runs all services in a shared Docker network

---

### 4️⃣ Access the Services

| Service       | URL                                                      |
| ------------- | -------------------------------------------------------- |
| Frontend      | [http://localhost:3000](http://localhost:3000)           |
| Backend API   | [http://localhost:8000](http://localhost:8000)           |
| Swagger Docs  | [http://localhost:8000/docs](http://localhost:8000/docs) |
| Mongo Express | [http://localhost:8081](http://localhost:8081)           |

**Mongo Express Login**

* Username: `admin`
* Password: `secret`

---

## 🧠 Key Concepts Demonstrated

* Docker Compose multi-service orchestration
* Environment-based configuration using `.env`
* MongoDB authentication and persistent volumes
* Container-to-container communication via service names
* Backend startup failure debugging
* Clean separation of frontend, backend, and database layers

---

## 🎨 UI Features

* Clean login and signup forms
* Simple navigation between login and signup
* Profile page displaying:

  * Avatar
  * Full name
  * User details in table format
* Responsive and readable layout

---

## ❌ Limitations (Intentional)

* No JWT authentication
* No logout functionality
* Passwords stored in plain text
* No session management
* No role-based access control

These limitations are intentional to keep the project focused on **learning fundamentals and infrastructure setup**.

---

## 🔮 Future Enhancements

* JWT-based authentication
* Password hashing (bcrypt)
* Logout and session handling
* Profile image upload
* Edit profile functionality
* CI/CD pipeline (GitHub Actions)
* Deployment on AWS EC2 / Kubernetes

---

## 🎓 Learning Outcomes

* Frontend–backend integration using REST APIs
* MongoDB CRUD operations with authentication
* Dockerizing multi-service applications
* Debugging container networking and environment issues
* Applying industry-style Git branching and workflows

---

### ✅ Recommended Additions

Create this file for clarity:

**`.env.example`**

```env
MONGO_USERNAME=your_username
MONGO_PASSWORD=your_password
```

---

## 📄 License

This project is created for **learning and educational purposes**.

---
