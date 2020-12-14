import paho.mqtt.client as paho  
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

broker = "192.168.137.20"
port = 1886

def on_publish(client, userdata, result):
    print("data publish: /n")
    pass


while (True):
    client = paho.Client("control1")
    client.on_publish = on_publish
    client.connect(broker,port)

    GPIO.output(8, GPIO.HIGH)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    sleep(1)
    re= client.publish("control","ON led 1")
    GPIO.output(10, GPIO.HIGH)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    sleep(1)
    re = client.publish ("control","ON led 2")
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    sleep(1)
    re = client.publish("control","ON led 3")



