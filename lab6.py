from turtle import *
import random
import math
colormode(255)


class ball(Turtle):
    def __init__(self, radius, color, speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)

ball1 = ball(300,"blue",400)
ball2 = ball(260,"red",270)

def random_color(ball):
    r = random.randint(0,256)
    g = random.randint(0,256)
    b = random.randint(0,256)
    ball.color(r,g,b)

def check_collision(ball1,ball2):
    x1=ball1.pos()[0]
    x2=ball2.pos()[0]
    y1=ball1.pos()[1]
    y2=ball2.pos()[1]
    if (ball1.radius + ball2.radius) >= math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2)):
        random_color(ball1)
        random_color(ball2)

check_collision(ball1,ball2)

