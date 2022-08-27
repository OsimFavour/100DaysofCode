from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("data.txt") as data:                  # reading the high score from data.txt
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self) -> None:
        self.clear()
        self.write(f"Score: {self.score}      High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:                # take note of this algorithm
            self.high_score = self.score
            with open("data.txt", mode="w") as data:    # writing to the data to change the current high score
                data.write(f"{self.high_score}")        # converting the data in data.txt to a string with the f string
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
