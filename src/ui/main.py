from turtle import Screen
from time import sleep
from src.model.snake import Snake
from src.model.food import Food
from src.model.scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake(scoreboard)
food = Food()


def run_game():
    while snake.game_continues():
        screen.update()
        sleep(0.05)
        snake.move()

        if snake.head.distance(food) < 14:
            scoreboard.increase_score()
            scoreboard.update_scoreboard()
            food.refresh()
            snake.add_piece()


def reset():
    snake.reset()
    scoreboard.reset()
    run_game()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.end_game, "q")
screen.onkey(reset, "space")

run_game()
scoreboard.game_over()
screen.exitonclick()
