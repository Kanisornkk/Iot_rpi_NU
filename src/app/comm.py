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

class MQTTConn:
    def __init__(self):
        self.client = mqqtt.Client()
        self.client.on_connect = self.on_conection
        #self.client.on_subscribe = on_subscription
        self.client.on_message = self.on_message
        self.client.connect(HIVEMQTT_BROKER, HIVEMQTT_PORT)
        self.client.loop_start()

    def publish(self, topic, message):
        self.client.publish(topic, message)



    def on_subscription(self, *args):
        print("subscribed: ",args)

    def on_conection(self, *args):
    #call back for when mqtt connects to the broker and prints out an acknowledgement and subscribes
        print("connected")
        self.client.subscribe(SUBSCRIBE_TOPIC)
    @staticmethod
    def on_message(client,user_data, msg: mqqtt.MQTTMessage):
        print("got message", msg.payload)

if __name__ == '__main__':
    client = MQTTConn()
    while True:
        client.publish("Naresuan/Tao",
                   "hello this is Tao")
        time.sleep(10)
