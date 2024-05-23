from turtle import Turtle
UP = 90
DOWN = 270
LEFT_POS = -350
RIGHT_POS = 350


class Paddle(Turtle):
    """Paddles for pong made of turtles"""

    def __init__(self, is_left):
        super().__init__()
        self.shape('square')
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.is_left = is_left
        self.position_paddle()

    def move_up(self):
        """Moves the paddle up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        """Moves the paddle down"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def position_paddle(self):
        """Positions the paddle on the screen according to self.is_left"""
        if self.is_left:
            self.goto(LEFT_POS, 0)
        else:
            self.goto(RIGHT_POS, 0)
