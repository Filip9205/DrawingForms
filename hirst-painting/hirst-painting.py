import random

import colorgram
import turtle

turtle.colormode(255)

timmy = turtle.Turtle()
timmy.penup()
timmy.speed(0)
timmy.hideturtle()



colors = colorgram.extract("image.jpg", 30)


extracted_colors = []

for color in colors:
    rgb = color.rgb
    red = rgb.r
    green = rgb.g
    blue = rgb.b
    tuple_colors = (red, green, blue)
    extracted_colors.append(tuple_colors)

y = 50
while y < 550:
    for _ in range(10):
        timmy.dot(20, random.choice(extracted_colors))
        timmy.forward(50)
    timmy.teleport(0, y)
    y += 50






screen = turtle.Screen()
screen.exitonclick()