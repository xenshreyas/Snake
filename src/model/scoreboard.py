from turtle import Turtle

TEXT_COLOR = "dark red"
SCORE_COLOR = "dark gray"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(SCORE_COLOR)
        self.penup()
        self.setposition(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.setposition(0, 0)
        self.color(TEXT_COLOR)
        self.write("GAME OVER", align="center", font=("Arial", 24, "underline"))

    def reset(self):
        self.clear()
        self.__init__()
        self.score = 0
        self.update_scoreboard()
