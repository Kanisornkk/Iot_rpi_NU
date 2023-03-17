# copyright (c) 2022 Kanisorn Kaewsrithong <kanisornka65@nu.ac.th>

"""
Communicate with the HIVEMQ broker to receive
sensor data, using the paho mqtt library
"""

__author__ = "Kanisorn Kaewsrithong"


# installed library
import paho.mqtt.client as mqtt

import final_gui #local file

# This is config of Naresuan/Kanisorn/final topic
HIVEMQTT_PORT = 1883  # CONSTANT
HIVEMQTT_BROKER = "broker.hivemq.com"
PUBLISH_TOPIC = "Naresuan/Kanisorn/final"
SUBSCRIBE_TOPIC = "Naresuan/Kanisorn/+"
NAME = "Tao"

# This is config of Naresuan/Final/Kanisorn/Tx topic
PUBLISH_TOPIC_Tx = "Naresuan/Final/Kanisorn/Tx"
SUBSCRIBE_TOPIC_Tx = "Naresuan/Final/Kanisorn/+"


class MQTTConn:
    def __init__(self, root: final_gui):

        self.root = root
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connection
        self.client.on_message = self.on_message

        self.client.connect(HIVEMQTT_BROKER, HIVEMQTT_PORT)
        self.client.loop_start()

        self.Pressing = final_gui.Pressing


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
        self.client.subscribe(SUBSCRIBE_TOPIC_Tx)

    def on_message(self, client, user_data, msg: mqtt.MQTTMessage):
        """
            Callback when receiving message
            Args:
            client:
            user_data:
            msg (mqtt.MQTTMessage): message received
        """

        if msg.topic == "Naresuan/Final/Kanisorn/Rx":
            msg_tx = int(msg.payload)**2
            self.client.publish(PUBLISH_TOPIC_Tx, msg_tx)


        print("got message: ", msg.payload)
        print("from topic: ", msg.topic)
        name = msg.topic.split('/')[-2]
        print("message from: ", name, '\n')



if __name__ == "__main__":
    test_client = None