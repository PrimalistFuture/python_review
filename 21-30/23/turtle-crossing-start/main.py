import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# instances
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen = Screen()
# screen settings
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move_up, "Up")


def conduct_turtle_dodge_car_game():
    """Conducts the game"""
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager.create_car()
        car_manager.move_cars()

        # detect collision with car
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

        # detect successful crossing
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increment_score()


conduct_turtle_dodge_car_game()
screen.exitonclick()
