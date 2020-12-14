import RPi.GPIO as GPIO
import paho.mqtt.client as paho
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#CHÂN TRIGGER
GPIO_TRIGGER = 18
#CHÂN ECHO
GPIO_ECHO = 24
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
broker = "169.254.168.205"
port = 1883

def on_publish(client, userdata, result):
	print("data publish: /n")
	pass
while True:
    client = paho.Client("control")
    client.on_publish = on_publish
    client.connect(broker,port)
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime=time.time()
    StopTime=time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    re = client.publish("control/ultra","khoang cach do duoc = %.1f cm," % distance)
    time.sleep(0.1)
        


