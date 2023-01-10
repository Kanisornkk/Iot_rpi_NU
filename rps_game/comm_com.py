# Copyright (c) 2022 Kyle Lopin <kylel@nu.ac.th>

"""
Communicate with the HIVEMQ broker to receive
sensor data, using the paho mqtt library
"""

__author__ = "Kanisorn Kaewsrithong"
COM_LIST = ['Rock', 'Scissors', 'Paper']

# installed library
import paho.mqtt.client as mqtt

import app #local file # for type hinting

HIVEMQTT_PORT = 1883  # CONSTANT
HIVEMQTT_BROKER = "broker.hivemq.com"
PUBLISH_TOPIC = "Naresuan/Tao"
PUBLISH_TOPIC_COM = "Naresuan/COMPUTER"
SUBSCRIBE_TOPIC = "Naresuan/+"
NAME = "Tao"
NAME_COM = "COMPUTER"

import random

COM_LISTS = ['Rock', 'Scissors', 'Paper']

class MQTTConn:
    def __init__(self, root: app):

        self.root = root
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connection
        self.client.on_message = self.on_message

        self.client.connect(HIVEMQTT_BROKER, HIVEMQTT_PORT)
        self.client.loop_start()

        self.RPS = app.RockPaperScissors



    def publish(self, message):
        """
        Send a message to the HIVE MQ broker using the PUBLISH_TOPIC
        Args:
            message (str): message to send
        """
        self.client.publish(PUBLISH_TOPIC, message)

    def publish_com(self, message_com):
        """
            Send a message to the HIVE MQ broker using the PUBLISH_TOPIC_COM
            Args:
                message (str): message to send
        """
        self.client.publish(PUBLISH_TOPIC_COM, message_com)


    def on_connection(self, *args):
        """ Call back for when mqtt connects to the broker
         and prints out an acknowledgement and subscribes """
        print("Connected")
        self.client.subscribe(SUBSCRIBE_TOPIC)

    def on_message(self, client, user_data, msg: mqtt.MQTTMessage):
        """
            Callback when receiving message
            Args:
            client:
            user_data:
            msg (mqtt.MQTTMessage): message received
        """
        self.msg_com = random.choice(COM_LISTS)
        print("got message: ", msg.payload)
        print("from topic: ", msg.topic)
        name = msg.topic.split('/')[-1]
        print("message from: ", name,'\n')
        if name == 'COMPUTER':
            print('----------------------------------------')
        else:
            self.publish_com(self.msg_com)
            self.root.change_status(self.msg_com)

if __name__ == "__main__":
    test_client = None