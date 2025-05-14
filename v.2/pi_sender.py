import serial
import paho.mqtt.client as mqtt
import time
import json

broker = "74.234.52.12"
port = 1883
topic = "sensor/data"

client = mqtt.Client()
client.connect(broker, port)

#Send data til VM
def upload():

    data = {
        "temperatur": temperatur,
        "latitude": latitude,
        "longitude": longitude,
        "xvalue": xvalue,
        "yvalue": yvalue,
        "zvalue": zvalue
    }

    client.publish(topic, json.dumps(data))
    print(f"Sendte data: {data}")
    time.sleep(5)  
    
#Split datastring
def split_coords(astring):
	"""Split astring on semi-colon and convert to floats."""
	temperatur, latitude, longitude, xvalue, yvalue, zvalue = astring.split(';')
	temperatur = float(temperatur)
	latitude = float(latitude)
	longitude = float(longitude)
	xvalue = float(xvalue)
	yvalue = float(yvalue)
	zvalue = float(zvalue)
	return (temperatur, latitude, longitude, xvalue, yvalue, zvalue)

#Modtag data fra arduino
ser = serial.Serial (port="/dev/ttyS0", baudrate=115200, timeout=.1)    #Open port ttyS0 with baud rate 9600
time.sleep(0.1) #wait for serial to open
while True:
	if (ser.inWaiting() > 0):
		time.sleep(0.01) 
		# read the bytes 
		received_data = ser.read(ser.inWaiting()).decode('ascii')
		temperatur, latitude, longitude, xvalue, yvalue, zvalue = split_coords(received_data)
		upload()
		print(received_data)
		time.sleep(0.50)       
#Modtag data slut