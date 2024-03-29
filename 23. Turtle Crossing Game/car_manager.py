from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []
        self.create_car()
        self.move_cars()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)   # it ensures every 6 times the while loop runs, a new car will be generated
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(x=300, y=random_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.setheading(180)
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT





