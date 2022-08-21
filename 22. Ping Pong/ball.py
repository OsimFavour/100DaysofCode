from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self): 
        new_x = self.xcor() + self.x_move  # increase in 10 pixels in the x-coordinate
        new_y = self.ycor() + self.y_move  # and same in the y-coordinate
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= - 1   # reverse the direction by multiplying it by -1
   
    def bounce_x(self):
        self.x_move *= - 1
        self.move_speed *= 0.9  # to increase the speed after collision

    def restart_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()


