# copyright (c) 2022 Kanisorn Kaewsrithong <kanisornka65@nu.ac.th>

"""
Communicate with the HIVEMQ broker to receive
sensor data, using the paho mqtt library
"""

__author__ = "Kanisorn Kaewsrithong"
COM_LIST = ['Rock', 'Scissors', 'Paper']

# installed library
import paho.mqtt.client as mqtt

import app_rps #local file # for type hinting

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
    def __init__(self, root: app_rps):

        self.root = root
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connection
        self.client.on_message = self.on_message

        self.client.connect(HIVEMQTT_BROKER, HIVEMQTT_PORT)
        self.client.loop_start()

        self.RPS = app_rps.RockPaperScissors



    def publish(self, message):
        """
        Send a message to the HIVE MQ broker using the PUBLISH_TOPIC
        Args:
            message (str): message to send
        """
        self.client.publish(PUBLISH_TOPIC, message)




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
        print("got message: ", msg.payload)
        print("from topic: ", msg.topic)
        name = msg.topic.split('/')[-1]
        print("message from: ", name,'\n')


        # if we get mesaeges from Computer, msg_com will change value following computer choice
        if name == 'Computer' and msg.payload == b'Rock':
            msg_com = 'Rock'
            self.root.change_status(msg_com)
            print('----------------------------------------------------------------------')

        elif name == 'Computer' and msg.payload == b'Scissors':
            msg_com = 'Scissors'
            self.root.change_status(msg_com)
            print('----------------------------------------------------------------------')

        elif name == 'Computer' and msg.payload == b'Paper':
            msg_com = 'Paper'
            self.root.change_status(msg_com)
            print('----------------------------------------------------------------------')


if __name__ == "__main__":
    test_client = None