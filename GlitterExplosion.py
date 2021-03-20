import turtle
import random
import math
import time

screen=turtle.Screen()
screen.tracer(0)
screen.bgcolor(0,0,0)

glitterCount = 0
exploded = False

glitter = []





class glitt(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    global glitterCount
    self.speed(0)
    self.shape('circle')
    self.x = 0
    self.y = 0
    self.xspd = random.random()*16-8
    self.yspd = random.random()*16
    
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    self.color(r,g,b)

    glitter.append(self)
    glitterCount+=1
  
  def move(self):
    self.yspd -= 0.2
    self.xspd *= 0.98
    self.yspd *= 0.98
    #print(self.yspd)
    self.x += self.xspd
    self.y += self.yspd
    self.goto(self.x, self.y)



launch=glitt()
launch.yspd = 13
launch.xspd = 0
launch.color(255,255,255)
screen.update()
time.sleep(2)

while(True):
  if(launch.y<0 and exploded == False):
    launch.hideturtle()
    launch.penup()
    exploded = True

    for i in range(100):
      glitters = glitt()
    
  for x in range(glitterCount):
    glitter[x].move()
  screen.update()