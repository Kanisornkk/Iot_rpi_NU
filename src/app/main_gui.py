# copyright (c) 2022 Kanisorn Kaewsrithong <kanisornka65@nu.ac.th>

""" Document string (doc string)
A grraphical user interface to observe sensor data from a remote sensor
througha mqtt communication channel
"""

___authore___ = "Kanisorn Kaewsrithong"

#libral
import tkinter as tk

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
        self.canvas.pack()

    def toggle_color(self):
        """ Change the color between red and green"""
        if self.color == 'red':
            self.color = 'green'
        elif self.color == 'green':
            self.color = 'red'
        self.canvas.itemconfig(self.circle, fill=self.color)


#make apython function to print "hello word"
#def-define

app = tk.Tk() #application a class of tkinter.Tk
app.geometry('400x600') #geometry is method of the tkinter.tk
status_btn=StatusButton(app)
print(status_btn)
status_btn2=StatusButton(app)
print(status_btn2)
tk.Button(app, text="Toggle Circle 1",
               command=status_btn.toggle_color).pack()

tk.Button(app, text="Toggle Circle 2",
               command=status_btn2.toggle_color).pack()


#make a button)
#Button takes 2 arguement,app-where to putbutton
#text-keyword
app.mainloop()  # mainloop is method of tkinter.tk methods are functions of classes
