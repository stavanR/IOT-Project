import paho.mqtt.client as mqtt
import time

temp = pre = hum = alert = 0

def on_message(mqttc, obj, msg):
	if msg.topic == "ALERT" :
		alert = int(str(msg.payload.decode("utf-8")))
		print("Uh oh, Something went wrong")

	elif msg.topic == "TEMPERATURE" :
		print(msg.topic + "  : " + str(msg.payload.decode("utf-8")))
		temp = int(str(msg.payload.decode("utf-8")))

	elif msg.topic == "PRESSURE" :
		print(msg.topic + "  : " + str(msg.payload.decode("utf-8")))
		pre = int(str(msg.payload.decode("utf-8")))

	elif msg.topic == "HUMIDITY" :
		print(msg.topic + "  : " + str(msg.payload.decode("utf-8")))
		hum = int(str(msg.payload.decode("utf-8")))
		print("\n")
	time.sleep(0.1)
	


mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.connect("broker.hivemq.com", 1883, 60)
mqttc.subscribe("TEMPERATURE", 0)
mqttc.subscribe("HUMIDITY", 0)
mqttc.subscribe("PRESSURE", 0)
mqttc.subscribe("ALERT", 0)
mqttc.loop_forever()
