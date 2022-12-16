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
PUBLISH_TOPIC = "Naresuan/Tao"
SUBSCRIBE_TOPIC = "Naresuan/+"
import main_gui
class MQTTConn:
    def __init__(self, root: main_gui.SensorUI):
        self.root =root
        self.client = mqqtt.Client()
        self.client.on_connect = self.on_conection
        #self.client.on_subscribe = on_subscription
        self.client.on_message = self.on_message
        self.client.connect(HIVEMQTT_BROKER, HIVEMQTT_PORT)
        self.client.loop_start()

    def publish(self, message):
        self.client.publish(PUBLISH_TOPIC,message)



    def on_subscription(self, *args):
        print("subscribed: ",args)

    def on_conection(self, *args):
    #call back for when mqtt connects to the broker and prints out an acknowledgement and subscribes
        print("connected")
        self.client.subscribe(SUBSCRIBE_TOPIC)

    def on_message(self,client,user_data, msg: mqqtt.MQTTMessage):
        print("got message", msg.payload)
        print("from topic", msg.topic)
        name = msg.topic.split('/')[-1]
        print("message from", name)
        self.root.toggle_status(name)




if __name__ == '__main__':
    client = MQTTConn()
    while True:
        client.publish("Naresuan/Tao",
                   "hello this is Tao")
        time.sleep(10)
