##scoreboard.py
from Tkinter import *

class Scoreboard:
    def __init__(self, canvas):
        #starting fuction
        self.value1 = 0
        self.value2 = 0
        self.score1 = canvas.create_text(625,456, fill = "blue", font = ("Purisa",15), text = "Robot 1 = " + str(self.value1))
        self.score2 = canvas.create_text(625,484, fill = "red", font = ("Purisa",15), text = "Robot 2 = " + str(self.value2))
        return

    def update_score1(self, canvas, score_increase):
        #used to update the scores
        self.value1 += score_increase
        canvas.itemconfig(self.score1, text = "Robot 1 = " + str(self.value1))
        
    def update_score2(self, canvas, score_increase):
        #used to update the scores for the second robot
        self.value2 += score_increase
        canvas.itemconfig(self.score2, text = "Robot 2 = " + str(self.value2))

    def get_winner(self):
        if self.value1 > self.value2:
            return "Robot 1"
        else:
            return "Robot 2"
