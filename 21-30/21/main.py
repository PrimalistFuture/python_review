from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# instances
SNAKE = Snake()
food = Food()
scoreboard = Scoreboard()
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
    # game flow
    while game_is_on:
        SCREEN.listen()
        SCREEN.onkey(SNAKE.up, "Up")
        SCREEN.onkey(SNAKE.down, "Down")
        SCREEN.onkey(SNAKE.left, "Left")
        SCREEN.onkey(SNAKE.right, "Right")

        SCREEN.update()
        time.sleep(0.1)
        SNAKE.move()
        # detect collision with food
        if SNAKE.head.distance(food) < 15:
            food.refresh()
            SNAKE.extend()
            scoreboard.increment_score()
        # detect collison with wall
        if SNAKE.head.xcor() > 280 or SNAKE.head.xcor() < -280 or SNAKE.head.ycor() > 280 or SNAKE.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()
        # detect collision with tail
        for segment in SNAKE.segments[1:]:
            if SNAKE.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()


conduct_game()
SCREEN.exitonclick()
