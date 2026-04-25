# Kubernetes Assignment – Flask Application Deployment

## 📌 Overview

This assignment demonstrates deploying a Dockerized Flask application on Kubernetes using Minikube.
The system is designed to be scalable, resilient, and configurable using core Kubernetes features.

---

## 🧱 Components Implemented

### 1. Deployment & ReplicaSet

* Runs the Flask application in multiple Pods
* Ensures high availability and self-healing

### 2. Service (NodePort)

* Exposes the application externally
* Accessible via `minikube service`

### 3. Horizontal Pod Autoscaler (HPA)

* Automatically scales Pods based on CPU usage
* Configuration:

  * Min replicas: 2
  * Max replicas: 5
  * Target CPU utilization: 50%

### 4. ConfigMap

* External configuration for the application
* Injects environment variable:

  * `APP_MESSAGE`

### 5. CronJob

* Periodically deletes application Pods
* Demonstrates Kubernetes self-healing (Deployment recreates Pods)

### 6. RBAC (Role-Based Access Control)

* Custom ServiceAccount (`pod-cleaner`)
* Role with permissions:

  * get, list, delete Pods
* RoleBinding to connect them

### 7. Liveness & Readiness Probes

* `/health` endpoint added to Flask app
* Liveness:

  * Restarts container if unhealthy
* Readiness:

  * Removes Pod from traffic if not ready

---

## 🚀 How to Run

```bash
minikube start

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f configmap.yaml
kubectl apply -f hpa.yaml
kubectl apply -f rbac.yaml
kubectl apply -f cronjob.yaml

minikube service flask-app
```

---

## 🔍 Verification Commands

```bash
kubectl get pods
kubectl get svc
kubectl get hpa
kubectl get cronjobs
```

---

## 📁 Files

```text
deployment.yaml
service.yaml
configmap.yaml
hpa.yaml
cronjob.yaml
rbac.yaml
```

---

## 🧠 Key Concepts

* Kubernetes Deployments and Services
* Autoscaling with HPA
* Configuration via ConfigMap
* RBAC security model
* Health checks (Liveness & Readiness)
* Automation with CronJobs

---

## ✅ Status

All required Kubernetes components were successfully implemented and tested.
