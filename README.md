# Auto Dealer CI/CD & Cloud Deployment

A containerized vehicle service management API built with **Python, FastAPI, PostgreSQL and Docker**, with a focus on implementing modern DevOps practices, CI/CD automation and cloud deployment.

## Project Overview

The Auto Dealer Service API provides a backend system for managing vehicle service bookings and tracking vehicle service history.

The project is designed to demonstrate how an application can be developed, tested, containerized, deployed and maintained using modern DevOps tools and automation practices.

The long-term goal is to build a reliable deployment workflow with automated testing, infrastructure as code, monitoring and deployment rollback capabilities.

## Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Containerization | Docker |
| Container Orchestration | Docker Compose |
| Testing | Pytest |
| Code Quality | Ruff |
| Version Control | Git & GitHub |
| CI/CD | GitHub Actions (planned) |
| Infrastructure as Code | Terraform (planned) |
| Cloud Platform | AWS (planned) |

## Current Features

- REST API for vehicle service bookings.
- Create and retrieve service bookings.
- Retrieve individual bookings by ID.
- Track vehicle service history.
- PostgreSQL database integration.
- Dockerized application using a multi-stage Dockerfile.
- Docker Compose configuration for application and database services.
- Container health checks.
- Persistent PostgreSQL storage using Docker volumes.
- Automated application tests using Pytest.
- Non-root application user inside the production container.
- Environment-based database configuration.

## Project Architecture

The current application consists of two main services:

1. **API Service:** A FastAPI application running inside a Docker container.
2. **Database Service:** A PostgreSQL database running in a separate Docker container.

Docker Compose manages the services, networking, health checks and persistent database storage.

```text
                 Client
                   |
                   | HTTP :8001
                   |
             +-------------+
             |  FastAPI    |
             |  API        |
             |  Container  |
             +-------------+
                   |
                   | SQLAlchemy
                   |
             +-------------+
             | PostgreSQL |
             | Container  |
             +-------------+
                   |
             Persistent Volume
```

## Project Structure

```text
auto-dealer-cicd-cloud-deployment/
│
├── app/
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── tests/
│   ├── conftest.py
│   └── test_bookings.py
│
├── terraform/
│   └── modules/
│
├── docs/
├── monitoring/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
├── .dockerignore
├── .env.example
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

Install the following tools:

- Python 3.14 or compatible version
- Docker Engine
- Docker Compose
- Git

### 1. Clone the repository

```bash
git clone https://github.com/ishotzng/auto-dealer-cicd-cloud-deployment.git

cd auto-dealer-cicd-cloud-deployment
```

### 2. Create a Python virtual environment

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements-dev.txt
```

### 4. Configure environment variables

Create your local environment file:

```bash
cp .env.example .env
```

Update `.env` with your own PostgreSQL credentials:

```env
POSTGRES_USER=autodealer
POSTGRES_PASSWORD=your_secure_password
POSTGRES_DB=auto_dealer
```

**Important:** Never commit your `.env` file or expose database credentials in a public repository.

### 5. Start the application

Build and start the services:

```bash
docker compose up -d --build
```

Check the running containers:

```bash
docker compose ps
```

### 6. Access the API

The API is available at:

- API Base URL: http://localhost:8001
- Health Check: http://localhost:8001/health
- Interactive API Documentation: http://localhost:8001/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API welcome message |
| GET | `/health` | Application health check |
| POST | `/bookings` | Create a service booking |
| GET | `/bookings` | Retrieve all bookings |
| GET | `/bookings/{booking_id}` | Retrieve a booking by ID |
| GET | `/vehicles/{vehicle_id}/history` | Retrieve vehicle service history |

### Example: Create a Booking

```bash
curl -X POST http://localhost:8001/bookings \
  -H "Content-Type: application/json" \
  -d '{
    "vehicle_id": "TOYOTA-001",
    "customer_name": "John Doe",
    "vehicle_make": "Toyota",
    "vehicle_model": "Camry",
    "service_type": "Engine Oil Change"
  }'
```

## Running Tests

Run the automated test suite:

```bash
python -m pytest -v
```

Check code quality using Ruff:

```bash
ruff check app tests
```

## Current Development Progress

- [x] FastAPI application development
- [x] Vehicle booking endpoints
- [x] SQLAlchemy database integration
- [x] PostgreSQL integration
- [x] Docker multi-stage build
- [x] Docker Compose configuration
- [x] Persistent database volume
- [x] Container health checks
- [x] Automated application tests
- [x] Git version control and GitHub repository

## Planned DevOps Roadmap

- [ ] GitHub Actions CI pipeline
- [ ] Automated linting and testing
- [ ] Container vulnerability scanning
- [ ] Docker image publishing to a container registry
- [ ] AWS cloud infrastructure provisioning with Terraform
- [ ] Automated application deployment
- [ ] Blue-green or rolling deployment strategy
- [ ] Deployment health checks and automatic rollback
- [ ] Secrets management
- [ ] Application monitoring and alerting
- [ ] Deployment documentation and operational runbook

## Project Goal

The objective is to develop an end-to-end CI/CD and cloud deployment workflow that demonstrates practical DevOps engineering skills.

The intended deployment targets include reliable application delivery, repeatable infrastructure provisioning, minimal downtime and improved application observability.

## Author

**Ishotzng**

GitHub: [@ishotzng](https://github.com/ishotzng)

---

*This project is actively under development as part of my hands-on DevOps engineering learning journey.*
