import paho.mqtt.client as mqtt
import sqlite3
import json

conn = sqlite3.connect("data.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS målinger (
    tid TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperatur REAL,
    latitude REAL,
    longitude REAL,
    xvalue REAL,
    yvalue REAL,
    zvalue REAL
)
""")
conn.commit()

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        temperatur = data["temperatur"]
        latitude = data["latitude"]
        longitude = data["longitude"]
        xvalue = data["xvalue"]
        yvalue = data["yvalue"]
        zvalue = data["zvalue"]
        print(f"Modtog: {data}")
        cursor.execute("INSERT INTO målinger (temperatur, latitude, longitude, xvalue, yvalue, zvalue) VALUES (?, ?, ?, ?, ?, ?)",
                       (temperatur, latitude, longitude, xvalue, yvalue, zvalue))
        conn.commit()
    except Exception as e:
        print("Fejl:", e)

client = mqtt.Client()
client.connect("localhost", 1883)
client.subscribe("sensor/data")
client.on_message = on_message

client.loop_forever()
