# Wisecow DevOps Assessment

## Project Overview

This project demonstrates the containerization, deployment, monitoring, and CI/CD automation of the Wisecow application as part of the AccuKnox DevOps Trainee Assessment.

The application generates random wisdom messages using `cowsay` and `fortune` packages and serves them through a lightweight web service.

---

# Problem Statement 1

## Features

* Dockerized Wisecow application
* Kubernetes deployment on Minikube
* Kubernetes Service exposure
* Ingress configuration
* TLS configuration
* GitHub Actions CI/CD pipeline
* Docker Hub image publishing

---

## Project Structure

```text
.
├── Dockerfile
├── README.md
├── wisecow.sh
├── k8s
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
├── scripts
│   ├── system_health_monitor.py
│   └── application_health_checker.py
└── .github
    └── workflows
        └── ci-cd.yml
```

---

## Docker Image

Docker Hub Repository:

```text
tapupan/wisecow:latest
```

Pull image:

```bash
docker pull tapupan/wisecow:latest
```

Run locally:

```bash
docker run -d -p 4499:4499 tapupan/wisecow:latest
```

---

## Kubernetes Deployment

Deploy resources:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
```

Verify deployment:

```bash
kubectl get pods
kubectl get svc
kubectl get ingress
```

---

## CI/CD Pipeline

GitHub Actions automatically:

1. Builds Docker image
2. Logs into Docker Hub
3. Pushes image to Docker Hub

The workflow is triggered automatically on every push to the `main` branch.

---

## Deployment Verification

Successfully verified:

* Docker container running locally
* Application accessible on localhost:4499
* Kubernetes pods running
* Service accessible through Minikube
* Docker image pushed to Docker Hub
* GitHub Actions workflow completed successfully

---

# Problem Statement 2

## Objective 1: System Health Monitoring Script

Implemented a Python-based monitoring solution for Linux system health.

### Features

* CPU usage monitoring
* Memory usage monitoring
* Disk usage monitoring
* Running process monitoring
* Threshold-based alert generation
* Alert logging support

### Run

```bash
python scripts/system_health_monitor.py
```

### Sample Output

```text
SYSTEM HEALTH REPORT

CPU Usage: 12.8%
Memory Usage: 79.7%
Disk Usage: 74.5%
Running Processes: 336

System is healthy.
```

---

## Objective 4: Application Health Checker

Implemented a Python-based application monitoring solution that verifies service availability using HTTP status codes.

### Features

* Application availability monitoring
* HTTP status code validation
* UP/DOWN status reporting
* Exception handling

### Run

```bash
python scripts/application_health_checker.py
```

### Sample Output

```text
APPLICATION HEALTH CHECK

URL: http://localhost:4499
HTTP Status Code: 200
Application Status: UP
```

---

# Technologies Used

* Docker
* Kubernetes
* Minikube
* GitHub Actions
* Docker Hub
* Python
* Linux
* Ingress NGINX
* TLS

---

# Author

**Breed Varpe**

GitHub:
https://github.com/Breedv
