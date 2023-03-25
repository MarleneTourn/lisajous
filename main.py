#Python Turtle - Lissajous Curve - www.101computing.net/python-turtle-lissajous-curve/
import turtle
from math import cos,sin
from time import sleep

window = turtle.Screen()
window.bgcolor("#FFFFFF")

myPen = turtle.Turtle()
myPen.hideturtle()
# myPen.tracer(0)
myPen.speed(4)
myPen.pensize(3)
myPen.color("#AA00AA")

myPen.penup()

A = 100
B = 100
a = 3 
b = 4
delta = 3.14/2
t=0

for i in range(0,1000):
    t+=0.01
    #Apply Lissajous Parametric Equations
    x = A * sin(a*t + delta) 
    y = B * sin(b*t) 

    myPen.goto(x,y)
    myPen.pendown()
    myPen.getscreen().update() 

sleep(0.5)

  

  
