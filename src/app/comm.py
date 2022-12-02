# copyright (c) 2022 Kanisorn Kaewsrithong <kanisornka65@nu.ac.th>

"""
Communicate with the HIVEMQ broker to receive sensor data, using the paho mqtt library
"""

___authore___ = "Kanisorn Kaewsrithong"

#standard libraries
import time

#installed library
import paho.mqtt.client as mqqtt

HIVEMQTT_PORT = 1883 #Constant
HIVEMQTT_BROKER = "broker.hivemq.com"
PYBLISH_TOPIC = "Naresuan/Tao"
SUBSCRIBE_TOPIC = "Naresuan/+"

def on_subscription(*args):
    print("subscribed: ",args)

def on_conection(*args):
    #call back for when mqtt connects to the broker and prints out an acknowledgement and subscribes
    print("connected")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client,user_data, msg: mqqtt.MQTTMessage):
    print("got message", msg.payload)


client = mqqtt.Client()
client.on_connect = on_conection
client.on_subscribe = on_subscription
client.on_message = on_message
client.connect(HIVEMQTT_BROKER,HIVEMQTT_PORT)
client.loop_start()
while True:
    client.publish("Naresuan/Tao",
                   "hello world is Tao")
    time.sleep(10)

