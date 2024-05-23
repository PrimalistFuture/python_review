from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    """Turtles made to look like scoreboard"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color('white')
        self.speed('fastest')
        self.update_scoreboard()

    def update_scoreboard(self):
        """Writes to scoreboard"""
        self.write(
            f"Score: {self.score}",
            align=ALIGNMENT,
            font=FONT
        )

    def game_over(self):
        """Game over"""
        self.goto(0, 0)
        self.write(
            "GAME OVER",
            align=ALIGNMENT,
            font=FONT
        )

    def increment_score(self):
        """Increments score"""
        self.clear()
        self.score += 1
        self.update_scoreboard()
