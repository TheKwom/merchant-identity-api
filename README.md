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
