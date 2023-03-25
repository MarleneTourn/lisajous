# Python Turtle - Lissajous Curve - www.101computing.net/python-turtle-lissajous-curve/
import turtle
from math import cos, sin
from time import sleep
import random


def ask_values():
    a = int(input("Dígame a: "))
    b = int(input("Dígame b: "))
    delta = float(input("Dígame delta mayor que 0: "))
    delta = 3.14 / delta
    t = int(input("Dígame t: "))
    return a, b, delta, t


def draw_line(a, b, delta, t):
    turtle.tracer(False)
    window = turtle.Screen()
    window.bgcolor("#006b9b")
    myPen = turtle.Turtle()
    myPen.hideturtle()
    myPen.speed(5)
    myPen.pensize(2)
    myPen.color("#AA00AA")
    myPen.color("#53e2f3")
    # colours = ['#b24a68', '#FAEBD7', '#F0FFFF', '#6495ED', '#008B8B', '#483D8B', '#20B2AA', '#9cb24a', '#abef57']

    while delta < 10:
        myPen.clear()
        myPen.penup()
        delta = delta + 0.1
        for i in range(0, 1000):
            t += 0.01
            # Apply Lissajous Parametric Equations
            x = 100 * sin(a * t + delta)
            y = 100 * sin(b * t)

            myPen.goto(x, y)
            myPen.pendown()
            myPen.getscreen().update()
    turtle.done()


if __name__ == "__main__":
    a, b, delta, t = ask_values()
    draw_line(a, b, delta, t)
