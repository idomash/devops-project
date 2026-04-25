# DevOps Course – Phase 1

## Overview

Simple Flask application containerized using Docker.

---

## Run with Docker

Build:
docker build -t devops-ido-flask-app .

Run:
docker run -p 5000:5000 devops-ido-flask-app

Open in browser:
http://localhost:5000

---

## Run with Docker Compose

docker-compose up

---

## Docker Hub

Image:
idomash97/devops-ido-flask-app:latest

Pull:
docker pull idomash97/devops-ido-flask-app:latest

Run:
docker run -p 5000:5000 idomash97/devops-ido-flask-app:latest

---

## Volumes

A Docker volume is used for demonstration of persistent storage:

* Local folder: ./data
* Container folder: /app/data

This allows data to persist even if the container is restarted or removed.

---

## Project Files

* FlaskApp.py
* Dockerfile
* requirements.txt
* docker-compose.yml
* data/ (volume directory)
