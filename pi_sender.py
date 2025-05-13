import paho.mqtt.client as mqtt
import time
import random
import json

broker = "DIN_AZURE_SERVER_IP"
port = 1883
topic = "sensor/data"

client = mqtt.Client()
client.connect(broker, port)

while True:
    temperatur = round(random.uniform(20.0, 25.0), 2)
    latitude = round(random.uniform(55.6, 55.8), 6)
    longitude = round(random.uniform(12.4, 12.6), 6)

    data = {
        "temperatur": temperatur,
        "latitude": latitude,
        "longitude": longitude
    }

    client.publish(topic, json.dumps(data))
    print(f"Sendte data: {data}")
    time.sleep(5)