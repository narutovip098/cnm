import paho.mqtt.client as paho
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
cb = Adafruit_DHT.DHT11
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#DHT11
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,GPIO.HIGH)

#DEN LED
GPIO.setup(19,GPIO.OUT)

broker = "169.254.168.205"
port = 1883

def on_publish(client, userdata, result):
	print("data publish: /n")
	pass

while(True):
    client = paho.Client("control1")
    client.on_publish = on_publish
    client.connect(broker,port)
    do_am,nhiet = Adafruit_DHT.read_retry(cb,4);
    if do_am is not None and nhiet is not None:
        GPIO.output(4,GPIO.HIGH)
        re = client.publish("control/temp", ("nhiet do = {0:0.1f}*C do am = {1:0.1f}%").format(nhiet,do_am))
        if nhiet <27 :
            GPIO.output(19,GPIO.HIGH)
            re = client.publish("control/temp", "Nhiet do thap, bat den suoi am cho ga")
        else:
            GPIO.output(19, GPIO.LOW)
        time.sleep(0.3)
    else:
        GPIO.output(4,GPIO.LOW)
        re = client.publish("control/temp", "Khong do duoc")
        time.sleep(0.3)
