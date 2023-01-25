# copyright (c) 2023 Kanisorn Kaewsrithong <kanisornka65@nu.ac.th>

"""
Display the data coming in from the sensor
Wrap a matplotlib pyplot in a tkinter frame
"""

___authore___ = "Kanisorn Kaewsrithong"

# srandard Libraries

from  datetime import datetime, timedelta

import tkinter as tk

# installed libraries
from  matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import  matplotlib.dates as mdates
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 40, 80, 160]
class Display(tk.Frame):
    """
    Display for sensor data implimented in a matplotlib.pypot and
    wrapped in tkinter Frame

    Attributes:
        figure (plt.Figure): figure of the displayed data
        axis (plt.axes): axis the data is plot on
        lines (list[matplotlib.line]): lines objects of the data
        canvas (FigureCanvasTkAgg): canvas displaying the data
    """
    def __init__(self, parent:tk.Tk):
        tk.Frame.__init__(self, master=parent)

        self.figure = plt.Figure(figsize=(6, 4))
        self.axis = self.figure.add_subplot()
        self.axis.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        self.lines = self.axis.plot([], [])
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def upddate_line(self, x_data: list, y_data: list):
        """
        update the data to be display

        Arg:
            x_data (list[floats]):x-axis coordinate of the data
            y_data (list[floats]):y-axis coordinate of the data

        """
        self.lines[0].set_xdata(x_data)
        self.lines[0].set_ydata(y_data)
        print(self.lines[0].get_xydata())
        now = x_data[-1]
        self.axis.set_xlim([now - timedelta(minutes=5),
                           now + timedelta(minutes=5)])
        self.axis.set_ylim([0, 40])
        self.canvas.draw()




