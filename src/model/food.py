from turtle import Turtle
import random

FOOD_COLOR = "light blue"


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.4, 0.4)  # stretches the turtle
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.setposition(random.randint(-250, 250), random.randint(-250, 250))
