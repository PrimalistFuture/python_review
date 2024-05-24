from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Turns the turtle into the scoreboard text"""

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write_score()

    def write_score(self):
        """Writes the score"""
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increment_score(self):
        """Clears the score, increments it, and rewrites it"""
        self.clear()
        self.level += 1
        self.write_score()

    def game_over(self):
        """Game over"""
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
