# Flask Application CI/CD Pipeline with Docker, Kubernetes, Helm and Jenkins

## Overview

This project was developed as part of a DevOps Engineer course.

The project demonstrates a complete DevOps workflow for a simple Flask application, including:

- Docker containerization
- Kubernetes deployment
- Helm chart packaging
- Git branching and pull requests
- Jenkins CI/CD pipeline with Build, Test and Deploy stages

---

## Application

The application is a simple Python Flask web application.

Endpoints:

- `GET /` - Returns the application message.
- `GET /health` - Returns `OK`.

The `/health` endpoint is used by the Jenkins pipeline during testing.

---

## Project Structure

```text
.
├── assignment-1-docker
├── assignment-2-kubernetes
├── assignment-3-helm
└── Jenkinsfile
```

---

## Phase 1 – Docker

The Flask application was containerized using Docker.

### Docker Image

```text
idomash97/devops-ido-flask-app:latest
```

### Build Image

From the project root:

```bash
docker build -t idomash97/devops-ido-flask-app:latest assignment-1-docker
```

### Dependency Version Pinning

```text
Flask==3.0.3
```

---

## Phase 2 – Kubernetes

The application was deployed to Kubernetes using Minikube.

### Resources

- Deployment
- Service
- Horizontal Pod Autoscaler (HPA)
- ConfigMap
- CronJob
- RBAC

---

## Phase 3 – Helm

The Kubernetes manifests were converted into a Helm Chart.

### Helm Commands

```bash
helm lint assignment-3-helm/flask-app
helm install flask-app assignment-3-helm/flask-app
helm upgrade --install flask-app assignment-3-helm/flask-app
helm package assignment-3-helm/flask-app
```

The package command creates a Helm artifact such as:

```text
flask-app-0.1.0.tgz
```

---

## CI/CD Pipeline

The Jenkins pipeline implements the following stages:

```text
Build → Test → Deploy
```

### Build

Builds the Docker image.

### Test

The Test stage performs:

- Helm validation (`helm lint`)
- Helm deployment (`helm upgrade --install`)
- Kubernetes rollout verification
- Application health check

### Deploy

The Deploy stage:

- Logs in to Docker Hub using Jenkins Credentials
- Pushes the Docker image to Docker Hub

Required Jenkins credential:

```text
dockerhub-credentials
```

---

## Git Workflow

The project uses GitHub with feature branches and pull requests.

Examples:

- phase3-helm
- jenkins-pipeline

These branches were merged into `main` after completion.

---

## Technologies Used

- Python
- Flask
- Docker
- Docker Hub
- Kubernetes
- Minikube
- Helm
- Git
- GitHub
- Jenkins

---

## Repository

https://github.com/idomash/devops-project

---

## Author

Ido Mashiah
