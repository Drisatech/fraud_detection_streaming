from kafka import KafkaConsumer, KafkaProducer
import joblib
import json

model = joblib.load("fraud_model.pkl")
scaler = joblib.load("scaler.pkl")

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

for message in consumer:
    data = message.value["features"]
    X = scaler.transform([data])
    prediction = int(model.predict(X)[0])
    result = {"prediction": prediction}
    producer.send("predictions", value=result)
