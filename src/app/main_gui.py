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


class SensorUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self) #initialize parent class
        self.comm = comm.MQTTConn()
        status_frame = tk.Frame(self, relief=tk.RIDGE, borderwidth=5)
        self.status_buttons = []
        print("1: ", self.status_buttons)
        for i in range(4):
            print("i= ", i)
            status_btn = StatusButton(status_frame)

        status_frame.pack(side=tk.TOP)
        tk.Button(self, text="Change status",
              command=status_btn.toggle_color).pack(side=tk.TOP)


    # make a button)
    # Button takes 2 arguement,app-where to putbutton
    # text-keyword




#make a variable to chang color


class StatusButton:
    """Display the status using a canvas
    Attributes:
        circle: object use to display status
        canvas (tk.Canvas):canvas the circle is in
        color (str):color the circle will show
    """
    def __init__(self,parent):
        self.color='red'
        self.canvas = tk.Canvas(parent, width=120, height=120)
        self.circle = self.canvas.create_oval(10, 10, 110, 110,
                                    fill=self.color)
        self.canvas.pack(side=tk.LEFT)

    def toggle_color(self):
        """ Change the color between red and green"""
        if self.color == 'red':
            self.color = 'green'
        elif self.color == 'green':
            self.color = 'red'
        self.canvas.itemconfig(self.circle, fill=self.color)


#make apython function to print "hello word"
#def-define

if __name__ == "__main__":

    app = SensorUI() #application a class of tkinter.Tk
    #app2 = SensorUI()
    app.geometry('400x600') #geometry is method of the tkinter.tk
    #app2.geometry('400x600')


    app.mainloop()  # mainloop is method of tkinter.tk methods are functions of classes
