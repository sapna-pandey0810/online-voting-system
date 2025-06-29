# 🗳️ Online Voting System

An Online Voting System developed using Python and web technologies. This project allows secure, transparent, and user-friendly online elections.

## 🚀 Features

- 🔐 User Authentication (Admin & Voter)
- 🧑‍💼 Candidate Management
- 🗳️ Real-time Voting
- 📊 Result Display
- 🧩 Modular Code with Django

## 🛠️ Tech Stack

- Python (Django)
- HTML / CSS
- SQLite3

## 📷 Screenshots

### 🏠 Home Page

![Home Page](screenshots/home_page.png)

### 🔐 Login Page

![Login Page](screenshots/login_page.png)

### 📝 Register Page

![Register Page](screenshots/register_page.png)

### 🗳️ Voting Page

![Voting Page](screenshots/voting_page.png)

### 📊 Result Page

![Result Page](screenshots/result_page.png)

## 📁 Project Structure

```ONLINE_VOTING_SYSTEM/
├── online_voting_system/ ← Project configuration folder
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── voting_app/ ← Main application folder
│ ├── migrations/
│ ├── static/
│ ├── templates/
│ │ ├── forget_password.html
│ │ ├── index.html
│ │ ├── login.html
│ │ ├── register.html
│ │ ├── results.html
│ │ └── voting.html
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
│
├── screenshots/ ← UI screenshots for README
│ ├── login_page.png
│ ├── register_page.png
│ └── ...
│
├── db.sqlite3 ← SQLite database file
├── manage.py ← Django entry point
└── README.md ← Project documentation```
