# Tasks API (Flask) 🚀

This is a small, opinionated REST API for managing tasks built with Flask and SQLAlchemy. It's intended as a lightweight starter project and example for learning how to structure a Flask app with a Blueprint, a simple model, and database access using SQLite. Perfect for prototyping or teaching REST concepts. 💡

## Features ✨

- ✅ CRUD endpoints for tasks (create, read, update, delete)
- 🗄️ SQLite database via Flask-SQLAlchemy
- 🧭 Blueprint-based controller in `controller/task_controller.py`
- 🧱 Simple model in `model/task.py`

## Repository layout 📁

```
app.py
extensions.py
README.md
requirements.txt
controller/
	└─ task_controller.py
model/
	└─ task.py
instance/
```

## Requirements 🧾

- Python 3.8+
- See `requirements.txt` for exact packages (Flask, Flask-SQLAlchemy)

## Quick start (Windows) 🛠️

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the app:

```powershell
python app.py
```

The API will be available at http://127.0.0.1:5000 by default. 🎯

## Endpoints 🔌

Base path: `/tasks`

- GET `/tasks`
	- Returns a JSON array of tasks. Each task has `id`, `title`, `description`, and `completed`.
	- Example response: `[{"id":1,"title":"Buy milk","description":"","completed":false}]`

- POST `/tasks`
	- Create a new task. Expects `application/json` body with at least `title`.
	- Body example: `{"title": "Buy milk", "description": "2 liters"}`
	- Returns the created task with HTTP 201 on success. 🆕

- PUT `/tasks/<int:task_id>`
	- Update an existing task. Accepts partial updates (fields not provided are left unchanged). ✍️
	- Returns the updated task on success.

- DELETE `/tasks/<int:task_id>`
	- Deletes the task. Returns a confirmation message on success. 🗑️

## Model 🧾

The `Task` model (in `model/task.py`) is a simple SQLAlchemy model with columns:

- `id` (int, primary key)
- `title` (string)
- `description` (text)
- `completed` (boolean)

## Recommendations & next steps 🚧

- Add input validation and serialization using Marshmallow or Pydantic.
- Add Flask-Migrate to support database migrations instead of relying on a plain SQLite file.
- Implement an application factory and configuration profiles (development/test/production).
- Add error handlers and structured logging for production readiness.
- Add tests (pytest + test client) and CI configuration. ✅

## Notes 📝

- This project is intentionally minimal. Use it as a learning scaffold or as a starting point for a small internal service.