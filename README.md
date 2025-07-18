# Fraud Detection with FastAPI, Docker, and Kafka

This project implements a real-time fraud detection system using a Machine Learning model served with **FastAPI**, containerized with **Docker**, and integrated with **Kafka** for streaming transactions. It is designed to scale as a microservice and be deployed on cloud platforms like **Azure Web App for Containers**.

---

## 🚀 Features

- ⚡ Real-time fraud detection API (`/predict`)
- 🧠 Pre-trained ML model using Scikit-learn
- 🔒 Secure scaling via Kafka event stream
- 🐳 Dockerized for easy deployment
- ☁️ Deployable to Azure App Service (Linux/Docker)
- 🧪 Includes Swagger UI documentation for testing

---

## 📁 Project Structure

fraud_detection/ ├── main.py               # FastAPI app ├── Dockerfile            # Build file for container ├── requirements.txt      # Python dependencies ├── fraud_model.pkl       # Trained ML model ├── scaler.pkl            # Preprocessing scaler ├── docker-compose.yml    # Local development with Kafka └── .github/ └── workflows/ └── deploy.yml    # CI/CD to Azure Web App

---

## 📦 Requirements

- Python 3.10+
- Docker
- (Optional) Docker Compose (for local Kafka testing)

---

## ⚙️ Installation & Local Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/fraud_detection_streaming.git
cd fraud_detection_streaming

2. Build and run with Docker:



docker build -t fraud-api .
docker run -p 8000:8000 fraud-api

3. Access the FastAPI docs:



> Open: http://localhost:8000/docs




---

🧪 API Usage

POST /predict

Request Body:

{
  "features": [value1, value2, ..., valueN]
}

Response:

{
  "prediction": 0   // 0: Not Fraud, 1: Fraud
}

> ⚠️ Make sure the feature list matches the shape of the trained model input.




---

🐳 Local Development with Kafka (Optional)

To simulate real-time streaming locally with Kafka:

docker-compose up

This starts:

Zookeeper

Kafka Broker

FastAPI container



---

☁️ Deployment on Azure Web App for Containers

1. Create an Azure Web App for Containers (Linux).


2. Add a GitHub Actions workflow using Azure publish profile.


3. Push to main branch to auto-deploy.



Azure will pull from your Dockerfile and run uvicorn.


---

🔐 Environment Secrets (CI/CD)

AZURE_WEBAPP_PUBLISH_PROFILE: From Azure Web App > "Get publish profile"

AZURE_CREDENTIALS: Azure service principal JSON (for azure/login GitHub Action)



---

✅ To Do

[ ] Integrate Azure Event Hub instead of local Kafka

[ ] Add monitoring with Azure Monitor or Prometheus

[ ] Train and upload updated model versions with MLflow



---

👨‍💻 Author

Aliyu Idris Adeiza
AI/ML Engineer | Materials Scientist | Tech Entrepreneur
LinkedIn: https://linkedin.com/in/aliyu-idris


---

📄 License

This project is open source under the MIT License.
