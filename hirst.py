# import colorgram
#
# colors = colorgram.extract("image.jpg", 20)
#
# colors_rgb = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     colors_rgb.append(rgb)
#
# print(colors_rgb)
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
timmy = Turtle()
timmy.speed(10)
timmy.shape("circle")
timmy.pensize(20)
timmy.penup()
timmy.goto(-300, -200)
y = -200
# timmy.backward(300)
# timmy.right(90)
# timmy.forward(200)

color_list = [(253, 251, 248), (254, 250, 252), (232, 251, 242), (198, 12, 32), (250, 237, 17),
              (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12),
              (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31),
              (60, 14, 8), (224, 141, 211), (10, 97, 61)]


def paint_row():
    for i in range(10):
        timmy.color(random.choice(color_list))
        timmy.stamp()
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()


for n in range(10):
    paint_row()
    timmy.penup()
    y = y + 50
    timmy.goto(-300, y)
    timmy.pendown()


screen = Screen()
screen.exitonclick()
