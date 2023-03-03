# copyright (c) 2022 Kanisorn Kaewsrithong <kanisornka65@nu.ac.th>

"""

"""

___authore___ = "Kanisorn Kaewsrithong"

# standard library
from datetime import datetime as dt
import json
import time

# installed libraries
import paho.mqtt.client as mqtt
from gpiozero import CPUTemperature

# local file
from config import *

client = mqtt.Client()
client.connect(HIVEMQTT_BROKER, HIVEMQTT_PORT)
client.loop_start()

while True:
    temperature = CPUTemperature()

    payload = {"datetime": dt.now().strftime("%Y-%m-%d %H:%M:%S"),
               "device": "device Tao",
               "temperature": temperature}
    client.publish(PUBLISH_DATA_TOPIC, json.dumps((payload)))

    # sleep for 5 second
    time.sleep(5)