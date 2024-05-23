from turtle import Turtle
DOWN = 270


class Median(Turtle):
    """Uses turtle to draw the median line"""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0, 300)
        self.draw_median()

    def draw_median(self):
        """Draws the median line"""
        self.setheading(DOWN)
        while self.ycor() > -300:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
