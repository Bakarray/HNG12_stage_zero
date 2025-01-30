# Task 1

This project implements a public API to retrieve basic information stored on the backend such as the registered email address, current datetime in ISO 8601 format, and the GitHub URL of the project's codebase.


## Setup Instructions (run the project locally)

1. Clone the repository:
   
   ```bash
   git clone https://github.com/Bakarray/HNG12
   cd HNG12/Task1
   ```

2. Install dependencies
   
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations and start the development server
   
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

4. Access the API at http://127.0.0.1:8000/api/info/


## API Documentation

### Endpoint
    GET /api/info/

### Request Format
No request body is required.

### Response Format
{
    "email": "poesitor1@gmail.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/bakarray/Task1"
}

### Backlink
    https://hng.tech/hire/python-developers