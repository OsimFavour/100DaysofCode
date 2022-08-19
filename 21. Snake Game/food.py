from turtle import Turtle
import random

class Food(Turtle):   # Inheriting from a Module Class
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # used to stretch the turtle half it's size along it's length and it's width
        self.color("blue")
        self.speed("fastest") 
        self.refresh()  

    def refresh(self):
        random_x = random.randint(-280, 280)  # let the food appear from -280 to 280 on the x-axis
        random_y = random.randint(-280, 280)  # and same at the y-axis
        self.goto(random_x, random_y)   