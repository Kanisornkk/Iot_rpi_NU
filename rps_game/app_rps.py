# copyright (c) 2022 Kanisorn Kaewsrithong <kanisornka65@nu.ac.th>

"""
Making a GUI to play Rock Paper Scissor game.
adding 3 buttons to the gui and a label that shows what you have picked
"""

___authore___ = "Kanisorn Kaewsrithong"

import tkinter as tk #libraly

class RockPaperScissors:
    """ make class to create GUI """
    def __init__(self, master):
        self.app = master
        self.app.title("Rock Paper Scissors IoT game") # Named to GUI

    # Create the buttons for the three options
        # Rock
        self.rock_button = tk.Button(self.app, text="Rock", command=self.rock)
        self.rock_button.pack()

        # Scissors
        self.scissors_button = tk.Button(self.app, text="Scissors", command=self.scissors)
        self.scissors_button.pack()

        # Paper
        self.paper_button = tk.Button(self.app, text="Paper", command=self.paper)
        self.paper_button.pack()

    # Create text for showing results
        # when we open GUI, it will has no text for result.
        self.result_text = tk.Label(self.app, text="")
        self.result_text.pack()

    def rock(self):
        """ if we click 'pick rock' button, it will show text as 'You picked Rock' """
        self.result_text.config(text="You picked Rock")

    def scissors(self):
        """ if we click 'pick scissors' button, it will show text as 'You picked Scissors' """
        self.result_text.config(text="You picked Scissors")

    def paper(self):
        """ if we click 'pick paper' button, it will show text as 'You picked Paper' """
        self.result_text.config(text="You picked Paper")


app = tk.Tk()
app.geometry('400x400') # size of gui
RockPaperScissors(app)
app.mainloop()
