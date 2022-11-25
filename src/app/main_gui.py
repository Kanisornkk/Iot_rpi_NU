# copyright (c) 2022 Kanisorn Kaewsrithong <kanisornka65@nu.ac.th>

""" Document string (doc string)
A grraphical user interface to observe sensor data from a remote sensor
througha mqtt communication channel
"""

___authore___ = "Kanisorn Kaewsrithong"

#libraly
import tkinter

#make a variable to chang color
color = 'red' #= assignment
#make apython function to print "hello word"
#def-define
def hello_World():
    #make it go green ->yelllow->red
    global color
    print("Hello World")
    if color == 'green' :
            color = 'yellow' #green ->yellow
        #== is comparison

    elif color == 'yellow':
            color = 'red' #yello ->red

    elif color== 'red' :
            color = 'green' #red->green



    canvas.itemconfig(circle, fill= color)

app = tkinter.Tk() #application a class of tkinter.Tk
app.geometry('400x600') #geometry is method of the tkinter.tk
canvas = tkinter.Canvas(app, width=120, height=120)
circle = canvas.create_oval(10, 10,110,110,
                            fill = color)
canvas.pack()
tkinter.Button(app, text="hello world",
               command=hello_World).pack()
#make a button)
#Button takes 2 arguement,app-where to putbutton
#text-keyword

app.mainloop() #mainloop is method of tkinter.tk
#methods are functions of classes