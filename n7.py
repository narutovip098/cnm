"""
DHCNTT13B
Do an nhom 7
Thanh vien nhom
1)Nguyen Truong Thinh - 17057881
2)Duong Van Tu - 17049351
3)Duong The Tai - 17011171
4)Truong Duc Trong - 17072371
GVHD:ThS.NguyenThanhThai
"""
import paho.mqtt.client as paho
import RPi.GPIO as GPIO 
import Adafruit_DHT
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(25,GPIO.IN)
GPIO.setup(7,GPIO.IN)
GPIO_TRIGGER = 18
GPIO_ECHO = 24
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(21,GPIO.IN)
broker = "192.168.1.87"
port = 1883
cb = Adafruit_DHT.DHT11
def on_publish(client, userdata, result):
	print("data publish: /n")
	pass

def pirSensor():
	client = paho.Client("bancong")
	client.on_publish = on_publish
	client.connect(broker,port)
	i=GPIO.input(7)
	if i==0:
		GPIO.output(17,GPIO.LOW)
		re = client.publish("bancong/pir","khong co trom")
		time.sleep(5)
	elif i==1:
		GPIO.output(17,GPIO.HIGH)
		re = client.publish("bancong/pir","co trom")
		time.sleep(5)

def dht():
    client = paho.Client("phongngu")
    client.on_publish = on_publish
    client.connect(broker,port)
    do_am,nhiet = Adafruit_DHT.read_retry(cb,25);
    if do_am is not None and nhiet is not None:
        re = client.publish("phongngu/tm",("nhiet do = {0:0.1f}*C do am = {1:0.1f}%").format(nhiet,do_am))
        if nhiet >= 30:
            GPIO.output(23,GPIO.HIGH)
            re = client.publish("phongngu/tm", "da bat quat!")
        else:
            GPIO.output(23, GPIO.LOW)
        time.sleep(2)
    else:
        GPIO.output(23,GPIO.LOW)
        re = client.publish("phongngu/tm","khong do duoc")
        time.sleep(0.5)
def ultrasonic():
	client = paho.Client("phongkhach")
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
	re = client.publish("phongkhach/ultrasonic","khoang cach do duoc = %.1f cm" % distance)
	time.sleep(5)
	if distance > 50:
		GPIO.output(8,GPIO.HIGH)
		re = client.publish("phongkhach/ultrasonic","chao ban ve nha!")
def gas():
	client = paho.Client("phongbep")
	client.on_publish = on_publish
	client.connect(broker,port)
	if(GPIO.input(21)==0):
		GPIO.output(26,GPIO.HIGH)
		re = client.publish("phongbep/gas", "ko Co Ga")
		time.sleep(0.1)
	else:
		GPIO.output(26,GPIO.LOW)
		re = client.publish("phongbep/gas", "Canh bao!!!Bi ro ri ga")
		time.sleep(0.2)
try:
	while True:
		#dht()
		#ultrasonic()
		gas()
		#pirSensor()
except KeyboardInterrupt:
	print("Tam biet")
	GPIO.cleanup()
