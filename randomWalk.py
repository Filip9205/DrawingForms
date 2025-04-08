import random
import turtle
import turtle as t

turtle.colormode(255)
timmy = t.Turtle()

timmy.pensize(10)
timmy.speed(5)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color


heading = [0, 90, 180, 270]

while 0 < 1:
    timmy.pencolor(random_color())
    timmy.setheading(random.choice(heading))
    timmy.forward(50)

screen = Screen()
screen.exitonclick()
