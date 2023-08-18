import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)


def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours = (r, g, b)
    return colours


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(1000):
    tim.color(randomColor())
    tim.forward(30)
    tim.setheading(random.choice(directions))
