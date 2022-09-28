import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
turtle.colormode(255)


def rand_clr():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


timmy.speed("fastest")


def draw_spiro(size_of_gap):
    for i in range(360//size_of_gap):
        timmy.pencolor(rand_clr())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+size_of_gap)


draw_spiro(5)
my_screen = Screen()
my_screen.exitonclick()
