import RPi.GPIO as GPIO
import paho.mqtt.client as paho
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#PIR
GPIO.setup(3,GPIO.IN)

#CÒI BÁO CHỐNG TRỘM
GPIO.setup(26,GPIO.OUT)

broker = "169.254.168.205"
port = 1883

def on_publish(client, userdata, result):
    print("data publish: /n")
    pass

while True:
    client = paho.Client("control")
    client.on_publish = on_publish
    client.connect(broker,port)
    pir = GPIO.input(3)
	
    if pir == 0:
        GPIO.output(26,GPIO.LOW)
        re = client.publish("control/pir","Khong co chuyen dong")
        time.sleep(5)
        
    elif pir == 1:
        GPIO.output(26,GPIO.HIGH)
        re = client.publish("control/pir","Phat hien co trom")
        time.sleep(5)
		
