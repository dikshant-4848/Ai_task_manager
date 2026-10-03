# 🤖 AI Task Manager

An AI-powered task management application built with **LangChain, LangGraph, Groq, SQL, and Streamlit**.

Instead of using traditional buttons/forms, you can manage your tasks simply by chatting with the AI.

For example:

> "Add a task to learn LangChain"

> "Show me all my tasks"

> "Mark task 1 as completed"

> "Delete the car drive task"

The AI agent understands the request and interacts with the SQL database accordingly.

---

## 🚀 Live Demo

**Live App:**
[https://ai-task-manager.streamlit.app/](https://aitaskmanager-dikshant4848.streamlit.app/)

---

## ✨ Features

* 🤖 AI-powered task management
* 💬 Natural-language interaction
* ➕ Create tasks using chat
* 📋 Read/list tasks
* ✏️ Update task status
* 🗑️ Delete tasks
* 🗄️ SQLite database integration
* 🔗 LangChain SQL Database Toolkit
* 🧠 LangGraph agent
* ⚡ Groq LLM
* 🌐 Streamlit web interface
* ☁️ Deployed on Streamlit Community Cloud

---

## 🏗️ Tech Stack

| Technology               | Purpose                      |
| ------------------------ | ---------------------------- |
| Python                   | Core programming language    |
| Streamlit                | Web application UI           |
| LangChain                | LLM and agent framework      |
| LangGraph                | Agent execution and memory   |
| Groq                     | LLM provider                 |
| SQLAlchemy / SQLDatabase | Database interaction         |
| SQLite                   | Task database                |
| Git & GitHub             | Version control & deployment |

---

## 🧠 How It Works

```text
             User
               │
               ▼
       ┌─────────────────┐
       │    Streamlit    │
       │       UI        │
       └────────┬────────┘
                │
                ▼
       ┌─────────────────┐
       │ LangChain Agent │
       └────────┬────────┘
                │
                ▼
          ┌───────────┐
          │   Groq    │
          │    LLM    │
          └─────┬─────┘
                │
                ▼
      ┌────────────────────┐
      │ SQLDatabaseToolkit │
      └─────────┬──────────┘
                │
                ▼
       ┌─────────────────┐
       │ SQLite Database │
       │     tasks       │
       └─────────────────┘
```

---

## 🗄️ Database Schema

The application uses a `tasks` table:

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT CHECK (
        status IN ('pending', 'in_progress', 'completed')
    ) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 💬 Example Commands

### Create a task

```text
Add a new task titled "Learn LangChain"
```

### View tasks

```text
Give me all tasks
```

### Update a task

```text
Mark task 1 as completed
```

### Delete a task

```text
Delete task 1
```

The agent converts the natural-language request into the appropriate SQL operation.

---

## 📁 Project Structure

```text
Ai_task_manager/
│
├── 4_sql_agent.py
├── requirements.txt
├── .gitignore
└── README.md
```

The SQLite database is created automatically when the application starts.

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/dikshant-4848/Ai_task_manager.git
```

### 2. Navigate to the project

```bash
cd Ai_task_manager
```

### 3. Create a virtual environment

```bash
python -m venv env
```

Activate it on Windows:

```powershell
.\env\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Add your API key

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

**Never commit your `.env` file to GitHub.**

### 6. Run the application

```bash
streamlit run 4_sql_agent.py
```

The application will open in your browser.

---

## ☁️ Deployment

This application is deployed using **Streamlit Community Cloud**.

Deployment flow:

```text
Local Project
     ↓
Git
     ↓
GitHub
     ↓
Streamlit Community Cloud
     ↓
Live Web Application
```

The `GROQ_API_KEY` is stored securely using Streamlit Secrets.

---

## 🔐 Environment Variables

The application requires:

```env
GROQ_API_KEY=your_groq_api_key
```

For Streamlit Cloud, configure it under:

```text
Manage App
    ↓
Settings
    ↓
Secrets
```

Example:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

---

## 🎯 Project Purpose

This project was built as a practical learning project to understand how **Generative AI, LangChain agents, SQL databases, and Streamlit** can work together to create an AI-powered application.

---

## 🔮 Future Improvements

* 🔐 User authentication
* 👤 Separate tasks for each user
* 🗃️ PostgreSQL database
* 📊 Task analytics dashboard
* 🔔 Task reminders
* 📅 Due dates
* 🏷️ Task categories and priorities
* 🎨 Improved UI
* 🧠 Persistent conversation memory

---

## 👨‍💻 Author

**Dikshant Rajput**

GitHub:
https://github.com/dikshant-4848

---

⭐ If you find this project useful, consider giving the repository a star!
