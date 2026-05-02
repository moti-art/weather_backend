# 🌦️ Weather Service (Backend Microservice)

[![CI for Weather Backend](https://github.com/moti-art/weather_backend/actions/workflows/ci.yaml/badge.svg)](https://github.com/moti-art/weather_backend/actions)

This microservice is a core component of the **Weather Dashboard Project**. It acts as a RESTful API gateway that fetches real-time weather data from the OpenWeatherMap external API and serves it to the frontend.

## 🚀 Features
* **Real-time Data:** Fetches live weather (Temp, Humidity, Wind) using OpenWeatherMap API.
* **Containerized:** Fully Dockerized for consistent deployment.
* **GitOps Ready:** Integrated with a full CI/CD pipeline that updates Helm charts automatically.
* **Resource Efficient:** Optimized with memory and CPU limits for AWS Free Tier.

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **Framework:** Flask
* **Containerization:** Docker
* **CI/CD:** GitHub Actions
* **Deployment:** Helm, ArgoCD, K3s (AWS EC2)

## 📂 API Endpoints

### Get Weather Data
Fetches current weather for a specific city.
* **URL:** `/weather/<city_name>`
* **Method:** `GET`
* **Success Response:** `200 OK`
```json
{
  "city": "Sydney",
  "description": "clear sky",
  "humidity": 65,
  "temperature": 22.5,
  "wind_speed": 4.1
}

💻 Local Development
Prerequisites
Python 3.x

Docker

OpenWeatherMap API Key

Running Locally
Clone the repo:

Bash
git clone [https://github.com/moti-art/weather_backend.git](https://github.com/moti-art/weather_backend.git)
cd weather_backend
Set Environment Variable:

Bash
export OPENWEATHER_API_KEY="your_api_key_here"
Install dependencies and run:

Bash
pip install -r requirements.txt
python app.py
🐳 Dockerization
Build the image:

Bash
docker build -t motinet/weather-backend:latest .
Run the container:

Bash
docker run -p 5000:5000 -e OPENWEATHER_API_KEY="your_key" motinet/weather-backend
🔄 CI/CD & GitOps Workflow
This repository follows the GitOps principle:

Push to Main: Triggers a GitHub Action.

Build & Push: A new Docker image is built and pushed to Docker Hub with a unique Git SHA tag.

Automated Manifest Update: The Action automatically clones the weather-gitops repository and updates the values-dev.yaml with the new Image Tag.

ArgoCD Sync: ArgoCD detects the change in the GitOps repo and performs a rolling update in the Kubernetes cluster (AWS).

Maintained by Moti Levi