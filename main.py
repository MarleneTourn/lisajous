#Python Turtle - Lissajous Curve - www.101computing.net/python-turtle-lissajous-curve/
import turtle
from math import cos,sin
from time import sleep
import random


def ask_values():
    A = int(input("Dígame el ancho del gráfico: "))
    B = int(input("Dígame el alto del gráfico: "))
    a = int(input("Dígame a: "))
    b = int(input("Dígame b: "))
    delta = float(input("Dígame delta mayor que 0 y menor o igual que 2: "))
    delta = 3.14/delta
    t = int(input("Dígame t: "))
    return A, B, a, b, delta, t

def draw_line(A, B, a, b, delta, t):
    window = turtle.Screen()
    window.bgcolor("#006b9b")
    myPen = turtle.Turtle()
    myPen.hideturtle()
    myPen.speed(10)
    myPen.pensize(2)
    myPen.color("#AA00AA")
    myPen.penup()
    colours = ['#b24a68', '#FAEBD7', '#F0FFFF', '#6495ED', '#008B8B', '#483D8B', '#20B2AA', '#9cb24a', '#abef57']

    for i in range(0,1000):
        t+=0.01
        #Apply Lissajous Parametric Equations
        x = A * sin(a*t + delta) 
        y = B * sin(b*t) 

        if i % 5 == 0:
            myPen.color(random.choice(colours))

        myPen.goto(x,y)
        myPen.pendown()
        myPen.getscreen().update() 
    sleep(0.5)


if __name__ == '__main__':
    A, B, a, b, delta, t = ask_values()
    draw_line(A, B, a, b, delta, t)

