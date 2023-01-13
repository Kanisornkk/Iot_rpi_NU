# copyright (c) 2022 Kanisorn Kaewsrithong <kanisornka65@nu.ac.th>

"""
Rock Paper Scissors game to have it sent the players choice to the hive mq broker
There will be a server running that will send the computers choice back to you.
Having GUI display the players choice and who won.
"""

___authore___ = "Kanisorn Kaewsrithong"


import tkinter as tk  # libraly

import comm_rps


class RockPaperScissors:
    """ make class to create GUI """

    def __init__(self, master: comm_rps):

        self.comm = comm_rps.MQTTConn(self)
        self.app = master


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

        #Variable for keeping player choice
        self.player_choice = " "

    def rock(self):
        """ if we click 'pick rock' button, it will show text as 'You picked Rock' """
        self.player_choice = 'Rock'
        self.person_text.config(text="You picked Rock")
        self.TEXT_ON()


    def scissors(self):
        """ if we click 'pick scissors' button, it will show text as 'You picked Scissors' """
        self.person_text.config(text="You picked Scissors")
        self.player_choice = 'Scissors'
        self.TEXT_ON()


    def paper(self):
        """ if we click 'pick paper' button, it will show text as 'You picked Paper' """
        self.player_choice = 'Paper'
        self.person_text.config(text="You picked Paper")
        self.TEXT_ON()

    def TEXT_ON(self):
        """
        Publish a choice which we choose in IoT
        """
        self.msg = self.player_choice
        self.comm.publish(self.msg)

    def change_status(self, msg_com):
        """
        Showing computer choice in GUI and rule of game
        """
        self.com_text.config(text="Computer picked "+ msg_com)

        if self.player_choice == msg_com:
            self.result_text.config(text="Draws\n"
                                         "(-_-)")

        elif self.player_choice == 'Rock' and msg_com == 'Scissors' \
                or self.player_choice == 'Scissors' and msg_com == 'Paper' \
                or self.player_choice == 'Paper' and msg_com == 'Rock':
            self.result_text.config(text="You Win \n"
                                         "(^_^)")

        else:
            self.result_text.config(text="You Lose\n"
                                         "(T_T)")


if __name__ == "__main__":
    app = tk.Tk()
    app.geometry('400x400')  # size of gui
    RockPaperScissors(app)
    app.mainloop()