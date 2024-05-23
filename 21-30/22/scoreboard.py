from turtle import Turtle


class Scoreboard(Turtle):
    """Scoreboard for pong"""

    def __init__(self, is_left):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.is_left = is_left
        self.position_scoreboard()
        self.write_score()

    def increment_score(self):
        """Increments the score for the given player"""
        self.clear()
        self.score += 1
        self.write_score()

    def write_score(self):
        """Writes the score"""
        self.write(
            f"{self.score}",
            align='center',
            font=('Courier', 24, 'normal')
        )

    def position_scoreboard(self):
        """Positions the scoreboard according to is_left"""
        if self.is_left:
            self.goto(-100, 260)
        else:
            self.goto(100, 260)
