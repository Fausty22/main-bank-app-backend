# Banking App — Backend

![Python](https://img.shields.io/badge/Language-Python-yellow)
![Flask](https://img.shields.io/badge/Framework-Flask-black)
![Docker](https://img.shields.io/badge/Container-Docker-blue)

## Overview
Backend API service for the three-tier banking application. Built with Python Flask, containerised with Docker and deployed to AWS EKS with RDS MySQL database.

## API Endpoints
| Endpoint | Method | Description |
|---|---|---|
| /health | GET | Health check |
| /api/status | GET | Infrastructure status |
| /api/accounts | GET | Bank accounts list |
| /api/transactions | GET | Transaction history |

## Tech Stack
- **Language:** Python 3.11
- **Framework:** Flask
- **Database:** AWS RDS MySQL
- **Container:** Docker
- **Registry:** Amazon ECR
- **Deployment:** Kubernetes on AWS EKS

## CI/CD Pipeline
Every push to main automatically:
1. Builds Docker image
2. Pushes to Amazon ECR
3. Argo CD detects change and deploys to EKS

## Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py

# Test endpoints
curl http://localhost:5000/health
curl http://localhost:5000/api/status
```

## Environment Variables
| Variable | Description |
|---|---|
| DB_HOST | RDS endpoint |
| DB_PORT | Database port (3306) |
| DB_NAME | Database name |
| DB_USER | Database username |
| DB_PASSWORD | Database password |
| APP_PORT | Application port (5000) |

## Author
**Faustina Nwokolo** — Cloud & DevOps Engineer