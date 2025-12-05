DevOps Assessment: CI/CD Pipeline Project

Name: Huzaifa
Roll No: BSSE23077
Subject: Software Design and Construction (SDC_LAB04)

📂 Project Structure

This repository contains the complete solution for the DevOps Class Assessment, covering Docker, Kubernetes, Docker Compose, and Jenkins.

project/
├── app/                  # Phase 1: Python Flask Application & Dockerfile
├── kubernetes/           # Phase 2: K8s Deployment & Service Manifests
├── docker-compose.yml    # Phase 3: Multi-service setup (App + Redis)
├── Dockerfile.agent      # Phase 4: Custom Jenkins Agent for CI/CD
├── Jenkinsfile           # Phase 4: CI/CD Pipeline Script
└── README.md             # Project Documentation


🚀 Phase 1: Container Bootcamp

Objective: Containerize a Python Flask application.

App Code: app/app.py (Includes error handling for missing DB).

Dockerfile: app/Dockerfile (Python 3.9-slim base).

How to Run:

cd app
docker build -t my-app:v1 .
docker run -p 5000:5000 my-app:v1


Access: http://localhost:5000

☸️ Phase 2: Kubernetes Deployment

Objective: Deploy the containerized app to a local Kubernetes cluster.

Manifests: kubernetes/deployment.yaml (Includes Deployment & NodePort Service).

How to Run:

kubectl apply -f kubernetes/deployment.yaml


Access: http://localhost:30005 (NodePort)

🐳 Phase 3: Multi-Service App (Docker Compose)

Objective: Run Frontend (Flask) and Backend (Redis) together with persistent storage.

Features: * Two Services: web-app and redis-db.

Volume: redis-data for data persistence.

Networking: Automatic service discovery.

How to Run:

docker-compose up -d --build


Access: http://localhost:5000 (Visits counter will work).

Debugging Challenges Completed:

[x] Add Volume: Data persists after restart.

[x] Restart Service: Restarted web-app independently.

[x] Kill & Recover: Verified app recovery after docker kill.

🤖 Phase 4: CI/CD War Zone (Jenkins)

Objective: Automate the Build-Test-Deploy lifecycle.

Pipeline Strategy: Jenkins-in-Docker with a Custom Build Agent.

Tools: Jenkins, Docker Pipeline Plugin, Kubernetes CLI.

Pipeline Stages:

Build: Creates the Docker image from app/.

Test: Runs a container test to verify start-up.

Deploy: Updates the Kubernetes cluster using kubectl.

How to Trigger:

Push code changes to GitHub.

Jenkins detects the change (or Manual Build).

Pipeline executes and updates the application on Port 31893.
