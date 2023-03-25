import turtle
import random
from math import cos, sin


def ask_values():
    a = int(input("Introduzca un valor a: "))
    b = int(input("Introduzca un valor b: "))
    delta = float(input("Introduzca un valor delta mayor que 0: "))
    delta = 3.14 / delta
    t = int(input("Introduzca un valor t: "))
    return a, b, delta, t


def draw_line(a, b, delta, t):
    turtle.tracer(False)
    window = turtle.Screen()
    window.bgcolor("#006b9b")
    myPen = turtle.Turtle()
    myPen.hideturtle()
    myPen.pensize(1)
    myPen.color("#ffffff")
    colors = ["#ffcccc", "#ffd9b3", "#ffffcc", "#c1ffc1", "#cce6ff", "#e6e6fa", "#f5e6ea"]

    while delta < 10:
        myPen.clear()
        delta += 0.025
        myPen.color(random.choice(colors))
        for i in range(0, 500):
            t += 0.06
            
            x = 225 * sin(a * t + delta)
            y = 225 * sin(b * t)

            myPen.goto(x, y)
            myPen.getscreen().update()
    turtle.done()


if __name__ == "__main__":
    a, b, delta, t = ask_values()
    draw_line(a, b, delta, t)
