from turtle import Turtle


class Ball(Turtle):
    """Turns a turtle into a pong ball"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Automatically moves the ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Inverses y_move"""
        self.y_move *= -1

    def bounce_x(self):
        """Inverses x_move"""
        self.x_move *= -1

    def reset_position(self):
        """Resets position of the ball, and reverses x direction"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    def increase_move(self):
        """Increases default move speed"""
        self.x_move += 5
        self.y_move += 5
