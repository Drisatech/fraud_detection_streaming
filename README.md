🧠 Fraud Detection Streaming System

🚀 Overview

This project implements a real-time fraud detection data pipeline that ingests streaming transactions, processes them in real time, and classifies fraudulent behavior using a trained machine learning model.
It’s built with FastAPI, Kafka (migrated to Azure Event Hub), and Docker, and deployed as a Web App for Containers on Azure.

The system demonstrates end-to-end data engineering, real-time processing, and cloud integration capabilities.


---

🏗️ Architecture Diagram

flowchart LR
A[Transaction Data Stream] --> B[Azure Event Hub / Kafka Producer]
B --> C[Streaming Consumer - FastAPI Service]
C --> D[ML Model - Fraud Detection]
D --> E[Storage - SQLite / PostgreSQL]
E --> F[Dashboard / REST API Output]


---

⚙️ Tech Stack

Category	Tools & Technologies

Programming	Python (FastAPI, Pydantic, Pandas, Scikit-learn)
Streaming	Apache Kafka → Azure Event Hub
Storage	SQLite (local), PostgreSQL (production)
Containerization	Docker
Deployment	Azure Web App for Containers
CI/CD	GitHub Actions
Messaging	Azure Event Hub Namespace: fraud-detection, Topic: fraud-detection-topic
Infrastructure	Azure CLI provisioning, GitHub integration



---

📦 Project Structure

fraud_detection_streaming/
│
├── app/
│   ├── main.py                # FastAPI main app with endpoints
│   ├── consumer.py            # Event Hub consumer logic
│   ├── producer.py            # Data producer simulation
│   ├── model.pkl              # Trained fraud detection model
│   ├── utils.py               # Helper functions (validation, logging)
│   └── config.py              # Azure Event Hub connection configs
│
├── docker/
│   └── Dockerfile             # Docker setup for container deployment
│
├── tests/
│   └── test_streaming.py      # Unit tests for streaming & prediction
│
├── requirements.txt
├── README.md
└── deploy.sh                  # Azure CLI deployment script


---

🔄 Pipeline Workflow

1. Ingestion:
The Kafka producer (or Azure Event Hub sender) streams transaction records into the Event Hub topic fraud-detection-topic.


2. Processing:
A consumer service (FastAPI backend) listens for incoming messages, transforms them into a structured format, and sends them to the model.


3. Prediction:
The pre-trained ML model classifies transactions as fraudulent or legitimate in real time.


4. Storage:
Results are logged and stored in SQLite/PostgreSQL for auditing and analytics.


5. Serving:
FastAPI endpoints expose fraud detection results through a RESTful API or web dashboard.




---

📊 Example Use Case

> The pipeline can be integrated with e-commerce or financial systems to detect fraudulent transactions in real time, reducing risk and improving decision accuracy.



Sample payload:

{
  "transaction_id": "TX123456",
  "amount": 1250.50,
  "user_age": 32,
  "location": "Lagos",
  "device_type": "Mobile"
}

Predicted response:

{
  "transaction_id": "TX123456",
  "is_fraud": true,
  "confidence": 0.92
}


---

🧪 Setup Instructions

Clone the Repository

git clone https://github.com/Drisatech/fraud_detection_streaming.git
cd fraud_detection_streaming

Create Virtual Environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Run Locally with Docker

docker-compose up --build

Run Producer & Consumer

python app/producer.py
python app/consumer.py

Start FastAPI Server

uvicorn app.main:app --reload

Visit: http://127.0.0.1:8000/docs


---

🧰 Key Features

✅ Real-time event ingestion (Kafka / Azure Event Hub)

✅ FastAPI microservice for streaming predictions

✅ Machine learning model integration

✅ Containerized with Docker for easy deployment

✅ Azure-based scalability and CI/CD setup



---

🌐 Deployment

Platform: Azure Web App for Containers

Event Stream: Azure Event Hub

CI/CD: GitHub Actions → Azure CLI (deploy.sh)

Monitoring: Container logs + Event Hub metrics



---

📈 Results / Output

Metric	Description

Latency	< 2 seconds from ingestion to classification
Throughput	1000+ events/minute (test load)
Accuracy	~94% model precision on test dataset


(Add your measured metrics here.)


---

👨‍💻 Author

Aliyu Idris Adeiza

Data Engineer | AI Systems Developer | Azure Practitioner

🌍 LinkedIn

💼 GitHub Portfolio

✉️ Email: drisatech@gmail.com



---

📚 License

This project is licensed under the MIT License — see the LICENSE file for details.


---

⭐ Project Summary (for Portfolio)

Aspect	Description

Goal	Real-time fraud detection pipeline
Focus Area	Data Engineering / Streaming Systems
Tech Stack	Python, FastAPI, Kafka, Azure, Docker
Deployment	Azure Web App for Containers
Outcome	Fully functional real-time prediction pipeline



---

Would you like me to create a short version of this README (1-page summary style) you can use as a portfolio landing section or GitHub profile highlight?

