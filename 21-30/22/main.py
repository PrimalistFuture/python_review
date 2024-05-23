from turtle import Screen
import time
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from median import Median

# instances
left_scoreboard = Scoreboard(True)
right_scoreboard = Scoreboard(False)
left_paddle = Paddle(True)
right_paddle = Paddle(False)
median = Median()
ball = Ball()
SCREEN = Screen()
# screen settings
SCREEN.setup(width=800, height=600)
SCREEN.bgcolor('black')
SCREEN.title("My Pong Game")
SCREEN.tracer(0)
# Event listeners
SCREEN.listen()
SCREEN.onkey(right_paddle.move_up, "Up")
SCREEN.onkey(right_paddle.move_down, "Down")
SCREEN.onkey(left_paddle.move_up, "w")
SCREEN.onkey(left_paddle.move_down, "s")


def conduct_game():
    """Conducts the game of pong"""
    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        SCREEN.update()
        ball.move()
        # detects collision with y-boundries
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        # detects collision with paddle
        if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()
            ball.move_speed *= 0.9
            # ball.increase_move()
        # detects ball passes right paddle
        if ball.xcor() > 380:
            left_scoreboard.increment_score()
            ball.reset_position()
        if ball.xcor() < -380:
            right_scoreboard.increment_score()
            ball.reset_position()


conduct_game()
SCREEN.exitonclick()
