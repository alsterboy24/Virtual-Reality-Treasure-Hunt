##robot.py

from turtle import RawTurtle
import turtle
from Tkinter import *
import math

class Robot:
    def __init__(self, scene, robot_id):
    #sets variables                     
        self.robot_id = robot_id
        self.turtle = RawTurtle(scene.canvas)
        self.scene = scene
        self.scr = self.turtle.getscreen()
        self.scr.setworldcoordinates(0, scene.height, scene.width, 0)
        self.turtle.penup()
        if robot_id == 1:
            self.turtle.color("blue")
        else:
            self.turtle.color("red")
    #create turtles sprite
##        self.turtle.register_shape("ship",((-7,-2),(-6,-1),(-3,0),(-3,1),(-2,5),
##                                           (0,7),(2,5),(3,1),(3,0),(6,-1),(7,-2),
##                                           (3,-1),(3,-2),(2,-7),(-2,-7),(-3,-2),
##                                           (-3,-1),(-2,-1),(-2,-2),(-1,-6),(1,-6),
##                                           (2,-2),(2,-1),(-2,-1),(-2,0),(2,0),
##                                           (2,1),(1,4),(0,5),(-1,4),(-2,1),
##                                           (-2,-1),(-3,-1))
##                         )
##        self.turtle.shape("ship")
##        self.turtle.shapesize(2,2)
    #place robot using reset
        self.reset()

    def reset(self):
    #set start positions for robots
        positions = [((15,15), 45), 
                    ((self.scene.width-15, 15), 135),
                    ((15, self.scene.height-15), 315),
                    ((self.scene.height-15, self.scene.width-15), 135)]
    #move robot to starting possition
        self.turtle.speed(0)
        self.turtle.setpos(positions[self.robot_id][0])
        #print positions[self.robot_id]
        self.turtle.left(positions[self.robot_id][1])
        self.turtle.forward(20)
        self.turtle.speed(0)
        self.turtle.screen.bgcolor("sky blue")

    def orientate(self, landmarks, canvas, goal):
##sd = shortest distance
##x1,x2,y1,y2 = circles corners
##lx,ly = length x/y
##h = hypothinus
##ln = landmark number
        sd = 40000000
        ln = 0
        
        for ID in landmarks:
            if canvas.itemcget(ID, "fill") == "dark green":
                ln+=1
                x1,y1,x2,y2 = canvas.coords(ID)
                lx = ((x1+x2)/2) - self.turtle.xcor()
                ly = ((y1+y2)/2) - self.turtle.ycor()
                h = math.sqrt(lx*lx + ly*ly)
                if h < sd:
                    sd = h
                    stored_ID = ID
                    stored_x = lx
                    stored_y = ly
        
        if ln == 0:
            stored_ID = goal
            x1,y1,x2,y2 = canvas.coords(goal)
            lx = ((x1+x2)/2) - self.turtle.xcor()
            ly = ((y1+y2)/2) - self.turtle.ycor()
            sd = math.sqrt(lx*lx + ly*ly)
            stored_x = ((x1+x2)/2) - self.turtle.xcor()
            stored_y = ((y1+y2)/2) - self.turtle.ycor()
        
        if sd < 37:
            return stored_ID
        
        if stored_x < 0:
            if stored_y < 0:
                new_heading = 180 + math.degrees(math.atan((-stored_y)/(-stored_x)))
            else:
                new_heading = 180 - math.degrees(math.atan(stored_y/(-stored_x)))
        elif stored_y < 0:
            new_heading = 360 - math.degrees(math.atan((-stored_y)/stored_x))
        else:
            new_heading = math.degrees(math.atan(stored_y/stored_x))

        self.turtle.seth(new_heading)
        return False

    def collisions_move(self, speed, depth):
    ##breaks the recursion if the robots get to close
        if depth > 10:
            return
    ##sets variables for checking collision
        turtle_x = self.turtle.xcor()
        turtle_y = self.turtle.ycor()
        t_heading = self.turtle.heading()
    ##variables used to check right
        xr = turtle_x + 15*math.cos(math.radians(self.turtle.heading()+30))
        yr = turtle_y + 15*math.sin(math.radians(self.turtle.heading()+30))
    ##variables used to check left
        xl = turtle_x + 15*math.cos(math.radians(self.turtle.heading()-30))
        yl = turtle_y + 15*math.sin(math.radians(self.turtle.heading()-30))
    ##check for the collision
        left = self.scene.canvas.find_overlapping(xl-1,yl-1,xl+1,yl+1)
        right = self.scene.canvas.find_overlapping(xr-1,yr-1,xr+1,yr+1)
        if left:
            ##turn away
            self.turtle.left(20)
            self.collisions_move(speed, depth+1)
            #self.turtle.forward(speed/5)
        elif right:
            ##turn away
            self.turtle.right(20)
            self.collisions_move(speed, depth+1)
            #self.turtle.forward(speed/5)
        else:
            ##else move forward
            self.turtle.forward(speed)
        return
