# copyright (c) 2022 Kanisorn Kaewsrithong <kanisornka65@nu.ac.th>

"""
Make a class to hold and process incoming
"""

___authore___ = "Kanisorn Kaewsrithong"

import random
#standard library
from dataclasses import dataclass
from datetime import datetime

import tkinter as tk

# local file

import display

@dataclass
class SensorData:
    """
    Dataclass to hold 1 sensor time series data

    Attributes:
        time (list[datetime]): time stamps of when ten sensors read data
        temperature (list[floats]): sensor data
        display (Display): child that will display the data of this class
    """
    time = []
    temperature = []

    def __init__(self, _parent):
        self.display = display.Display(_parent)
        self.display.pack()

    def add_data(self, time: datetime, temp: float):
        """
        Append new receive data from a sensor and add it to the existing data
        Call the Display child to update the user's view of the data
        """
        self.time.append(time)
        self.temperature.append(temp)

        self.display.upddate_line(self.time, self.temperature)



if __name__ == '__main__':
    _parent = tk.Tk()# main_gui
    sensor_data = SensorData(_parent)

    # use a lamda function to pass arguments
    tk.Button(_parent, text='Update data',
              command= lambda: sensor_data.add_data(
                  datetime.now(), random.randrange(20, 35))).pack()
    _parent.mainloop()
