from turtle import Turtle

TEXT_COLOR = "dark red"
SCORE_COLOR = "dark gray"
VICTORY_COLOR = "green"

PATH = "data/high_score.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(PATH) as file:
            self.high_score = int(file.read())
        self.color(SCORE_COLOR)
        self.penup()
        self.setposition(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            with open(PATH, mode="w") as file:
                file.write(str(self.score))
            self.high_score = self.score
            self.setposition(0, 240)
            self.write(f"High Score: {self.high_score}", align="center", font=("Courier", 20, "normal"))
        self.score = 0
        self.clear()
        self.color(SCORE_COLOR)
        self.setposition(0, 270)
        self.update_scoreboard()

