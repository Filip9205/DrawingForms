from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")


for _ in range(20):
    timmy.forward(50)
    timmy.penup()
    timmy.forward(50)
    timmy.pendown()









screen = Screen()
screen.exitonclick()