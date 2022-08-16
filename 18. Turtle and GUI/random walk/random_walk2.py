from turtle import Turtle
import random

tim = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim.pensize(6)
# tim.hideturtle()
tim.speed(0)
directions = [0, 90, 180, 270]

motion = 0
while motion < 500:
    tim.color(random.choice(colours))
    tim.setheading(random.choice(directions))
    tim.forward(20)
    motion += 1
     