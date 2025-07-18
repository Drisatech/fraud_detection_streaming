from confluent_kafka import Producer
import json

conf = {
    'bootstrap.servers': 'fraud-deatection.servicebus.windows.net:9093',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': '$ConnectionString',
    'sasl.password': 'Endpoint=sb://fraud-deatection.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=<your-access-key>',
}

producer = Producer(conf)

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

data = {
    "feature1": 10.5,
    "feature2": 2.3,
    "feature3": 4.5,
    "feature4": 1.2
}

topic = 'fraud-detection-topic'
producer.produce(topic, value=json.dumps(data), callback=delivery_report)
producer.flush()