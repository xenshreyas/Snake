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
snake = Snake()
food = Food()


def run_game():
    while True:
        screen.update()
        sleep(0.05)
        snake.move()

        if snake.head.distance(food) < 14:
            scoreboard.increase_score()
            scoreboard.update_scoreboard()
            food.refresh()
            snake.add_piece()

        for piece in snake.body[1:]:
            if snake.head.distance(piece) < 10:
                scoreboard.reset()
                snake.reset()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset()
            snake.reset()


def reset():
    snake.reset()
    scoreboard.reset()
    run_game()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(screen.bye, "Escape")
screen.onkey(reset, "space")

run_game()
screen.exitonclick()
