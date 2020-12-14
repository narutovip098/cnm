import paho.mqtt.client as paho
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#LED
GPIO.setup(19,GPIO.OUT)

#Set up địa chỉ cho PI
broker = "169.254.168.205"
port = 1883
sub_topic = "control/led"
client = paho.Client()
def on_message(client, userdata, message):
    print('Message is: ')
    print(str(message.payload))
    data = str(message.payload.decode())
    if data == 'on':
        GPIO.output(19,GPIO.HIGH)
    elif data == 'off':
        GPIO.output(19,GPIO.LOW)
def on_connect(client, userdata, flag, rc):
    print('connection returned' + str(rc))
    client.subscribe(sub_topic)
client.connect(broker,port)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()