# copyright (c) 2022 Kanisorn Kaewsrithong <kanisornka65@nu.ac.th>

"""
Make a graphical user interface with 1 button, that when pressed will publish to
the HIVE MQTT broker to the topic "Naresuan/{Name}/Final", the message "Hello World"

"""

___authore___ = "Kanisorn Kaewsrithong"

import tkinter as tk  # library

import comm_final  # local file


class Pressing:

    """ make class to create GUI """

    def __init__(self, master: comm_final):
        self.comm = comm_final.MQTTConn(self)
        self.app = master

        self.app.title("Communicated with Mqtt")  # Named to GUI

        self.PUBLISH_BUTTON = tk.Button(self.app, text="press",
                                        command=self.Pressing_Button)
        self.PUBLISH_BUTTON.pack()  # Create the button

        self.message = "Hello World"

    def Pressing_Button(self):
        """ if we pressed the button, it will publish our message to mqtt"""
        self.comm.publish(self.message)


if __name__ == "__main__":
    app = tk.Tk()
    app.geometry('400x400')  # size of gui
    Pressing(app)
    app.mainloop()
