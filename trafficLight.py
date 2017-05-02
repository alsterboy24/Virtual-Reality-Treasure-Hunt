##trafficLight.py

from Tkinter import*
from time import sleep
from random import randint

class Trafficlight:
    def __init__(self, Canvas):
        self.canvas = Canvas
        x = 700
        y= 450
        self.lightcase = self.canvas.create_rectangle(x-5,y-5,x+45,y+45, fill = "white")
        self.light = self.canvas.create_oval(x,y,x+40,y+40, fill = "green")
        self.i = 0
        
    def trafficlight_check(self):
        if self.i < 50:
            self.i += 1
        else:
            self.canvas.itemconfig(self.light, fill = "red")
            self.canvas.update()
            sleep(randint(1, 4))
            self.canvas.itemconfig(self.light, fill = "green")
            self.canvas.update()
            self.i = 0
        return
