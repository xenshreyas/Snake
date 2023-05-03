import _tkinter
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 15

EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

SNAKE_COLOR = "spring green"


class Snake:
    def __init__(self):
        self.body = []
        self.initialize_snake()
        self.head = self.body[0]

    def initialize_snake(self):
        for position in STARTING_POSITIONS:
            piece = Turtle("square")
            piece.color(SNAKE_COLOR)
            piece.penup()
            piece.setposition(position)
            self.body.append(piece)

    def move(self):
        for piece in range(len(self.body) - 1, 0, -1):
            new_x = self.body[piece - 1].xcor()
            new_y = self.body[piece - 1].ycor()
            self.body[piece].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != SOUTH:
            self.head.seth(NORTH)

    def down(self):
        if self.head.heading() != NORTH:
            self.head.seth(SOUTH)

    def left(self):
        if self.head.heading() != EAST:
            self.head.seth(WEST)

    def right(self):
        if self.head.heading() != WEST:
            self.head.seth(EAST)

    def add_piece(self):
        new_x = self.body[len(self.body) - 1].xcor()
        new_y = self.body[len(self.body) - 1].ycor()
        position = (new_x, new_y)

        new_piece = Turtle("square")
        new_piece.color(SNAKE_COLOR)
        new_piece.penup()

        new_piece.setposition(position)
        self.body.append(new_piece)

    def reset(self):
        for piece in self.body:
            piece.hideturtle()
        self.body.clear()
        self.initialize_snake()
        self.head = self.body[0]
