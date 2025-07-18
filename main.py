from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("fraud_model.pkl")
scaler = joblib.load("scaler.pkl")

class Transaction(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(data: Transaction):
    X = scaler.transform([data.features])
    prediction = model.predict(X)[0]
    return {"prediction": int(prediction)}
