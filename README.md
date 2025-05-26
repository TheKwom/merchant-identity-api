# Merchant Identity API

A backend service built with FastAPI to manage merchant data and identity.  
This project demonstrates core skills in building scalable backend systems, asynchronous APIs, and background task processing — aligned with the responsibilities of a Software Engineer I role on Affirm’s Merchant Data Platform team.

---

## Features

- Create, read, and list merchants with key identity and risk fields.
- Background task to enrich merchant data asynchronously.
- Async database operations using SQLAlchemy and `databases` package.
- Simple REST API with FastAPI and Pydantic data validation.
- Designed for easy extension with real-world backend concepts.

---

## Tech Stack

- Python 3.12+
- FastAPI
- SQLAlchemy 2.0
- `databases` async DB toolkit
- SQLite (for local development)
- Uvicorn (ASGI server)

---

## Getting Started

### Prerequisites

- Python 3.10+
- Git
- (Optional) Virtual environment tool like `venv`

### Installation

1. Clone the repository:

````bash
git clone https://github.com/<your-github-username>/merchant-identity-api.git
cd merchant-identity-api
````

2. Create and activate a virtual environment:

````bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
.\venv\Scripts\activate    # Windows
````

3. Install dependencies:

````bash
pip install -r requirements.txt
````

4. Initialize the database:

````bash
python init_db.py
````

### Running the API

````bash
uvicorn main:app --reload
````
The API will be available at http://127.0.0.1:8000.

## API Endpoints

| Method | Path              | Description                   |
|--------|-------------------|------------------------------|
| GET    | `/`               | Health check endpoint         |
| POST   | `/merchants`      | Create a new merchant         |
| GET    | `/merchants`      | List all merchants            |
| GET    | `/merchants/{id}` | Get a merchant by ID          |

## Background Processing

Merchant data enrichment runs as a background task upon creation, simulating risk analysis by assigning a random risk score and flag.

