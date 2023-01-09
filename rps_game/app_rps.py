# copyright (c) 2022 Kanisorn Kaewsrithong <kanisornka65@nu.ac.th>

"""
Making a GUI to play Rock Paper Scissor game.
adding 3 buttons to the gui and a label that shows what you have picked
"""

___authore___ = "Kanisorn Kaewsrithong"

import comm_person
import tkinter as tk  # libraly

import random

COM_LIST = ['Rock', 'Scissors', 'Paper']


class RockPaperScissors:
    """ make class to create GUI """

    def __init__(self, root):
        self.comm_person = comm_person.MQTTConn(self)
        self.app = root
        self.app.title("Rock Paper Scissors IoT game")  # Named to GUI

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
        self.person_text = tk.Label(self.app, text="")
        self.person_text.pack()

        self.com_text = tk.Label(self.app, text="")
        self.com_text.pack()

        self.result_text = tk.Label(self.app, text="", fg="red")
        self.result_text.pack()

    def rock(self):
        """ if we click 'pick rock' button, it will show text as 'You picked Rock' """
        self.player_choice = 'Rock'
        self.person_text.config(text="You picked Rock")
        self.com()

    def scissors(self):
        """ if we click 'pick scissors' button, it will show text as 'You picked Scissors' """
        self.person_text.config(text="You picked Scissors")
        self.player_choice = 'Scissors'
        self.com()

    def paper(self):
        """ if we click 'pick paper' button, it will show text as 'You picked Paper' """
        self.player_choice = 'Paper'
        self.person_text.config(text="You picked Paper")
        self.com()

    def com(self):
        self.com_choice = random.choice(COM_LIST)
        self.com_text.config(text="Computer picked " + self.com_choice)
        self.msg = self.player_choice
        self.comm_person.publish(self.msg)


        if self.player_choice == self.com_choice:
            self.result_text.config(text="Draws\n"
                                         "(-_-)")

        elif self.player_choice == 'Rock' and self.com_choice == 'Scissors' \
                or self.player_choice == 'Scissors' and self.com_choice == 'Paper' \
                or self.player_choice == 'Paper' and self.com_choice == 'Rock':
            self.result_text.config(text="You Win \n"
                                         "(^_^)")

        else:
            self.result_text.config(text="You Lose\n"
                                         "(T_T)")


app = tk.Tk()
app.geometry('400x400')  # size of gui
RockPaperScissors(app)
app.mainloop()