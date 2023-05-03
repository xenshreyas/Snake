from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 15

EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

SNAKE_COLOR = "spring green"


class Snake:
    def __init__(self, scoreboard):
        self.scoreboard = scoreboard
        self.continues = True
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
        self.check_collision()
        for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].setposition(new_x, new_y)
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

    def end_game(self):
        self.continues = False
        self.scoreboard.game_over()

    def game_continues(self):
        return self.continues

    def add_piece(self):
        new_x = self.body[len(self.body) - 1].xcor()
        new_y = self.body[len(self.body) - 1].ycor()
        position = (new_x, new_y)

        new_piece = Turtle("square")
        new_piece.color(SNAKE_COLOR)
        new_piece.penup()

        new_piece.setposition(position)
        self.body.append(new_piece)

    def check_collision(self):
        for piece in self.body[1:]:
            if self.head.distance(piece) < 10:
                self.end_game()

        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            self.end_game()

    def reset(self):
        for piece in self.body:
            piece.setposition(1000, 1000)
        self.body.clear()
        self.initialize_snake()
        self.head = self.body[0]
        self.continues = True
