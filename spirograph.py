import random
import turtle


turtle.colormode(255)
timmy = turtle.Turtle()

timmy.speed(0)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color


for i in range(0, 360):
    timmy.pencolor(random_color())
    timmy.circle(100)
    timmy.setheading(i)
    print(timmy.heading())


screen = turtle.Screen()
screen.exitonclick()