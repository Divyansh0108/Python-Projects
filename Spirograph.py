from turtle import *
from random import *

size_of_gap = int(input("Enter the size of gap: "))

turtle = Turtle()
colormode(255)


def randomColor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


turtle.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        for _ in range(100):
            turtle.color(randomColor())
            turtle.circle(100)
            turtle.setheading(turtle.heading() + 10)
            
draw_spirograph

screen = Screen()
screen.exitonclick()
