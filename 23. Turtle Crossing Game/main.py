import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forwards, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()   # creates a new car every 0.1 seconds after the screen update
    car_manager.move_cars()

    # Detect collision with Car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect collision with wall & Successful crossing
    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.restart_position()
        car_manager.level_up()


screen.exitonclick()
