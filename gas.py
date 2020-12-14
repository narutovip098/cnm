import RPi.GPIO as GPIO
import paho.mqtt.client as paho
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#GAS
GPIO.setup(21,GPIO.IN)

#CÒI
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
	if(GPIO.input(21)==0):
		re = client.publish("control/gas", "KHONG CO GAS")
		GPIO.output(26,GPIO.HIGH)
		print("KHONG CO GAS")
		time.sleep(1)
	else:
		re = client.publish("control/gas", "CO GAS CHAY NHA KIA BA CON")
		GPIO.output(26,GPIO.LOW)
		print("CO GAS CHAY NHA KIA BA CON")
		time.sleep(1)
		
		
