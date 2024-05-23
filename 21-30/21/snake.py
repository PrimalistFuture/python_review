from turtle import Turtle

STARTING_LENGTH = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """I am a snake"""

    def __init__(self):
        self.segments = []
        self.create_snake(STARTING_LENGTH)
        self.head = self.segments[0]

    def create_snake(self, length):
        """Creates a snake of length equal to STARTING_LENGTH"""
        for _ in range(length):
            tur = Turtle("square")
            self.segments.append(tur)

    def add_segment(self, position):
        """Adds a segment to the snake"""
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Adds a new segment to the snake"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """The snake moves forward automatically"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def give_color(self):
        """Colors the segments of the snake white"""
        for segment in self.segments:
            segment.color('white')

    def position_snake(self):
        """Places the snake at the start of the board"""
        x_cord = 0
        for segment in self.segments:
            segment.penup()
            segment.setposition(x_cord, 0)
            x_cord -= 20

    def up(self):
        """Moves the snake up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Moves the snake up"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Moves the snake up"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Moves the snake up"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
