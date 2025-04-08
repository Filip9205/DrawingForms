from turtle import Turtle, Screen
import random
timmy = Turtle()
colors = ["red", "blue", "yellow", "orange", "pink", "green", "black", "coral", "aqua", "azure"]
number_of_sides = 3

while number_of_sides < 10:
    timmy.pencolor(random.choice(colors))
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        timmy.forward(100)
        timmy.right(angle)
    number_of_sides += 1




screen = Screen()
screen.exitonclick()
