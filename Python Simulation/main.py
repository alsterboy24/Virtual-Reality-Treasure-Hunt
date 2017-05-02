##main.py

from Tkinter import *
from random import randint
from turtle import RawTurtle
from time import sleep

from robot import Robot
from trafficLight import Trafficlight
from scoreboard import Scoreboard

class Scene(Frame): ##main canvas class (creating the window)
    def __init__(self, master=None): ##passing the Tk root + options
        Frame.__init__(self, master) ##constructing the parent class
        self.parent = master ##keeping root for future reference
        self.width = 750 ##keeping width + height for future reference in class
        self.height = 500
        self.landmarks = []
        self.robots = []
        self.goal_id = None
        self.traffic_state = None
        self.robot_stopped = None

        self.parent.title("R2D2 Treasure Islands") ##naming window
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        
        self.file_menu = Menu(menubar)

        self.canvas = Canvas(self, width=self.width, height=self.height, bg="sky blue") ##init drawing canvas
        self.canvas.pack()
        self.pack()

        self.populate()
    
    def process(self):
        i = 1
        while i == 1:
        ##check thr traffic lights
            self.traffic_light.trafficlight_check()
        ##orientate the robots
            ID = self.robot1.orientate(self.landmarks, self.canvas, self.goal_id)
            if ID != False:
                self.canvas.itemconfig(ID, fill = "brown")
                self.score_board.update_score1(self.canvas, 10)
                if self.goal_id == ID:
                    self.score_board.update_score1(self.canvas, 40)
                    self.end_race(self.score_board.get_winner())
            ID = self.robot2.orientate(self.landmarks, self.canvas, self.goal_id)
            if ID != False:
                self.canvas.itemconfig(ID, fill = "brown")
                self.score_board.update_score2(self.canvas, 10)
                if self.goal_id == ID:
                    self.score_board.update_score2(self.canvas, 40)
                    self.end_race(self.score_board.get_winner())
        ##move the robots based on collisions
            self.robot1.collisions_move(5,1)
            self.robot2.collisions_move(5,1)

    def check_overlapping(self, x, y, size):
        return self.canvas.find_overlapping(x-20, y-20, x+size+20, y+size+20)

    def populate(self):
        self.robot1 = Robot(self,1)
        self.robot2 = Robot(self,2)

        self.traffic_light = Trafficlight(self.canvas)

        self.score_board = Scoreboard(self.canvas)

        num = 31
        goal = randint(0, num-1)

        for sq in range(num): 
            if sq == goal:
                sq_size = 30
            else:
                sq_size = 50
                
            x = randint(30, self.width - sq_size - 30) 
            y = randint(30, self.height - sq_size - 30)
            while self.check_overlapping(x, y, sq_size): 
                x = randint(30, self.width - sq_size - 30) 
                y = randint(30, self.height - sq_size - 30)
            if sq == goal:
                self.goal_id = self.canvas.create_oval(x, y, x + sq_size, y + sq_size, fill="gold", width=1)
            elif sq%2==0:
                obst_id = self.canvas.create_oval(x, y, x + sq_size, y + sq_size, fill="dark green", width=1)
            else:
                obst_id = self.canvas.create_oval( x, y, x + sq_size, y + sq_size, fill="brown", width=1)
            
            self.landmarks.append(obst_id)
        
        self.process()
    
    def repopulate(self):
        self.canvas.delete("all")
        self.canvas.pack()
        #self.reset_menu()
        self.populate()

    def end_race(self, winner):
        i=1
        self.canvas.delete("all")
        self.canvas.pack()
        win_text = winner + " is the winner!"
        self.canvas.create_text(self.width/2,self.height/2,font = ("Purisa",50), text = win_text )
        self.canvas.update()
        print "blah"
        sleep(5)
        self.repopulate()
                    
        
if __name__ == "__main__":
    root = Tk()
    sc = Scene(master=root)
    root.mainloop()
