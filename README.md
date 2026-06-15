# Wisecow DevOps Assessment

## Project Overview

This project demonstrates the containerization, deployment, and CI/CD automation of the Wisecow application as part of the AccuKnox DevOps Trainee Assessment.

The application generates random wisdom messages using cowsay and fortune packages and serves them through a lightweight web service.

---

## Features

- Dockerized Wisecow application
- Kubernetes deployment on Minikube
- Kubernetes Service exposure
- Ingress configuration
- TLS configuration
- GitHub Actions CI/CD pipeline
- Docker Hub image publishing

---

## Project Structure

```text
.
├── Dockerfile
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

tapupan/wisecow:latest

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

Verify:

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

Triggered on every push to the main branch.

---

## Deployment Verification

Successfully verified:

- Docker container running locally
- Application accessible on localhost:4499
- Kubernetes pods running
- Service accessible through Minikube
- Docker image pushed to Docker Hub
- GitHub Actions workflow completed successfully

---

## Author

Breed Varpe

GitHub:
https://github.com/Breedv

# Wisecow DevOps Assessment

## Project Overview

This project demonstrates the containerization, deployment, and CI/CD automation of the Wisecow application as part of the AccuKnox DevOps Trainee Assessment.

The application generates random wisdom messages using cowsay and fortune packages and serves them through a lightweight web service.

---

## Features

- Dockerized Wisecow application
- Kubernetes deployment on Minikube
- Kubernetes Service exposure
- Ingress configuration
- TLS configuration
- GitHub Actions CI/CD pipeline
- Docker Hub image publishing

---

## Project Structure

```text
.
├── Dockerfile
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

tapupan/wisecow:latest

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

Verify:

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

Triggered on every push to the main branch.

---

## Deployment Verification

Successfully verified:

- Docker container running locally
- Application accessible on localhost:4499
- Kubernetes pods running
- Service accessible through Minikube
- Docker image pushed to Docker Hub
- GitHub Actions workflow completed successfully

---

## Author

Breed Varpe

GitHub:
https://github.com/Breedv
