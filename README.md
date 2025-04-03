# Task Management API

A Flask-based REST API for managing tasks with MongoDB.

## Setup

1. Clone the repository
```bash
git clone <your-repository-url>
cd <project-directory>
```

2. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Unix/macOS
# OR
.venv\Scripts\activate  # On Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create .env file and add your MongoDB URL
```bash
mongodb_url=your_mongodb_connection_string
```

5. Run the application
```bash
python app.py
```

## API Endpoints

- POST /addTask - Create a new task
- GET /allTasks - Get all tasks
- GET /task/<task_id> - Get task by ID 