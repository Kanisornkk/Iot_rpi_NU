# copyright (c) 2022 Kanisorn Kaewsrithong <kanisornka65@nu.ac.th>

""" Document string (doc string)
A grraphical user interface to observe sensor data from a remote sensor
througha mqtt communication channel
"""

___authore___ = "Kanisorn Kaewsrithong"

#libral
import tkinter as tk

#local files
import comm

NAMES = ["Kyle", "Tao", "Sudarat", "Chatpon"]

class SensorUI(tk.Tk):
    def __init__(self):

        tk.Tk.__init__(self) #initialize parent class
        self.comm = comm.MQTTConn(self)
        status_frame = tk.Frame(self, relief=tk.RIDGE, borderwidth=5)
        self.status_buttons = []



        for i in range(4):

            status_btn = StatusButton(status_frame, NAMES[i])
            self.status_buttons.append(status_btn)

        self.running = False
        status_frame.pack(side=tk.TOP)
        self.button = tk.Button(self, text="Turn On",
              command=self.button_click)
        self.button.pack(side=tk.TOP)


    # make a button)
    # Button takes 2 arguement,app-where to putbutton
    # text-keyword

    def button_click(self):
        if self.running: #if true turn off sensor
            self.running =False
            msg = "Off"
            self.button.config(text="Turn On")
        else:

            self.running = True
            msg= "On"
            self.button.config(text="Turn Off")

        self.chang_status("Tao", self.running)
        self.comm.publish(msg)

    def chang_status(self, name, _running):
        index = NAMES.index(name)
        self.status_buttons[index].toggle_color(_running)




#make a variable to chang color


class StatusButton(tk.Frame):
    """Display the status using a canvas
    Attributes:
        circle: object use to display status
        canvas (tk.Canvas):canvas the circle is in
        color (str):color the circle will show
    """
    def __init__(self,parent, name):
        tk.Frame.__init__(self, master=parent)
        self.color='red'
        self.canvas = tk.Canvas(self, width=120, height=120)
        self.circle = self.canvas.create_oval(10, 10, 110, 110,
                                    fill=self.color)
        self.canvas.pack(side=tk.TOP)
        tk.Label(self, text=name, font=42).pack(side=tk.TOP)
        self.pack(side=tk.LEFT)

    def toggle_color(self, state):
        """ Change the color between red and green"""
        if state:
            self.color = 'green'
        else:
            self.color = 'red'
        self.canvas.itemconfig(self.circle, fill=self.color)


#make apython function to print "hello word"
#def-define

if __name__ == "__main__":

    app = SensorUI() #application a class of tkinter.Tk
    #app2 = SensorUI()
    app.geometry('600x400') #geometry is method of the tkinter.tk
    #app2.geometry('600x400')


    app.mainloop()  # mainloop is method of tkinter.tk methods are functions of classes
