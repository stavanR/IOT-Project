import paho.mqtt.client as mqtt 
from random import randrange
import time

mqttBroker ="broker.hivemq.com" 
client = mqtt.Client("Temperature_Outside")
client.connect(mqttBroker) 

alert = 0

while True:
    temp = randrange(25,30)
    pre = randrange(850,900)
    hum = randrange(10,15)

    if (temp > 28) or (pre >= 895) or (hum >= 14) :
        alert = 1 
        print("alert = " + str(alert))
        client.publish("ALERT", alert)

    time.sleep(0.1)
    print("Temprature = " + str(temp))
    client.publish("TEMPERATURE", temp)

    time.sleep(0.1)
    print("Pressure = " + str(pre))
    client.publish("PRESSURE", pre)

    time.sleep(0.1)
    print("Humidity = " + str(hum))
    client.publish("HUMIDITY", hum)

    print("\n")
    time.sleep(1)
