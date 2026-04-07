# 🚀 GitHub Cloud Connector (Django)

## 📌 Overview

This project is a **GitHub Cloud Connector** built using Django and Django REST Framework.
It integrates with the GitHub API to perform real-world actions such as fetching repositories and creating issues.

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* Requests Library
* GitHub REST API

---

## 🔐 Authentication

This project uses a **GitHub Personal Access Token (PAT)** for authentication.

The token is stored securely in a `.env` file and loaded using `python-dotenv`.

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/panchalpunam/github-cloud-connector.git
cd github-cloud-connector
```

### 2. Create virtual environment

  python -m venv venv

  #### Activate virtual environment

  On Windows:
  venv\Scripts\activate

  On macOS/Linux:
  source venv/bin/activate


### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` file

```env
GITHUB_TOKEN=your_github_token_here
```

### 5. Run Server

```bash
python manage.py runserver
```

---

## 🌐 API Endpoints

### 🔹 1. Fetch User Repositories

**GET**

```
/api/github/repos/<username>/
```

📌 Example:

```
/api/github/repos/octocat/
```

---

### 🔹 2. Create Issue in Repository

**POST**

```
/api/github/create-issue/<owner>/<repo>/
```

📌 Request Body:

```json
{
  "title": "Test Issue",
  "body": "Created via API"
}
```

---

### 🔹 3. List Issues from Repository

**GET**

```
/api/github/issues/<owner>/<repo>/
```

📌 Description:
Fetches all issues from a given repository.

📌 Example:

```
/api/github/issues/octocat/hello-world/
```

---


## ✅ Features

* GitHub API integration
* Token-based authentication
* Clean architecture (service layer)
* RESTful API design
* Error handling

---

## 📂 Project Structure

```
github_connector/
│
├── github_api/
│   ├── services/
│   │   └── github_service.py
│   ├── views.py
│   ├── urls.py
│
├── github_connector/
│   └── settings.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## 🎯 Key Highlights

* Demonstrates integration with external APIs
* Implements both GET and POST operations
* Follows clean and modular backend design

---

## ⚠️ Notes

* Ensure your GitHub token has `repo` permissions
* `.env` file is excluded using `.gitignore` for security

---


