from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
NORTH = 90


class Player(Turtle):
    """The turtle"""

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.speed('fastest')
        self.penup()
        self.setheading(NORTH)
        self.go_to_start()

    def move_up(self):
        """Moves the turtle up"""
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        """Detects at top of screen"""
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        """Go to the start"""
        self.goto(STARTING_POSITION)
