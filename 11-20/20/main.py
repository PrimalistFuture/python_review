from turtle import Turtle, Screen
import time
from snake import Snake

tim = Turtle("square")
tom = Turtle("square")
tam = Turtle("square")

SNAKE = Snake()

SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.bgcolor('black')
SCREEN.title("My Snake Game")
SCREEN.tracer(0)


def conduct_game():
    """Conducts the snake game"""
    # setup
    game_is_on = True
    SNAKE.give_color()
    SNAKE.position_snake()
    SCREEN.update()

    while game_is_on:
        SCREEN.listen()
        SCREEN.onkey(SNAKE.up, "Up")
        SCREEN.onkey(SNAKE.down, "Down")
        SCREEN.onkey(SNAKE.left, "Left")
        SCREEN.onkey(SNAKE.right, "Right")
        SCREEN.update()
        time.sleep(0.1)
        SNAKE.move()


conduct_game()
SCREEN.exitonclick()
