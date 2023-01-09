# Copyright (c) 2022 Kyle Lopin <kylel@nu.ac.th>

"""
Communicate with the HIVEMQ broker to receive
sensor data, using the paho mqtt library
"""

__author__ = "Kanisorn Kaewsrithong"

# standard libraries
import time

# installed library
import paho.mqtt.client as mqtt

import app_rps

# local fi # for type hinting

HIVEMQTT_PORT = 1883  # CONSTANT
HIVEMQTT_BROKER = "broker.hivemq.com"
PUBLISH_TOPIC = "Naresuant/Tao"
SUBSCRIBE_TOPIC = "Naresuant/+"
NAME = "Tao"


class MQTTConn:
    def __init__(self, root: app_rps) -> object:
        self.root = root
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connection
        self.client.on_message = self.on_message
        self.client.connect(HIVEMQTT_BROKER, HIVEMQTT_PORT)
        self.client.loop_start()

    def publish(self, message):
        self.client.publish(PUBLISH_TOPIC, message)

    def on_connection(self, *args):
        """ Call back for when mqtt connects to the broker
         and prints out an acknowledgement and subscribes """
        print("Connected")
        self.client.subscribe(SUBSCRIBE_TOPIC)

    def on_message(self, client, user_data, msg: mqtt.MQTTMessage):
        print("got message: ", msg.payload)
        print("from topic: ", msg.topic)
        print("message from: ", NAME)


