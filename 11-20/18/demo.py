from turtle import Turtle, Screen
import heroes  # installed with pip install heroes in terminal
import random
COLORS = ['red', 'orange', 'yellow', 'green',
          'blue', 'indigo', 'purple', 'black']
DIRECTIONS = [0, 90, 180, 270]
tim = Turtle()
tim.shape('turtle')
tim.color('red')

# draws a square


def draw_square():
    """Draws a square"""
    for _ in range(4):
        tim.forward(100)
        tim.left(90)


# draws a dashed line
# could have used penup() and pendown()
def draw_dashed_line():
    """Draws a dashed line"""
    X = 0
    for _ in range(10):
        tim.forward(10)
        X += 20
        tim.teleport(X)


def draw_shape(sides):
    """Draws a a regular polygon with the input amount of sides"""
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.left(angle)


def draw_many_polygons():
    """Instructs the tim the turtle to draw polygons, changing color each time.Could refactor to make use of COLORS."""
    side_and_colors = {3: 'red', 4: 'orange', 5: 'yellow', 6: 'green',
                       7: 'blue', 8: 'indigo', 9: 'purple', 10: 'black'}
    for sides in side_and_colors:
        tim.color(side_and_colors[sides])
        draw_shape(sides)


def random_walk(steps):
    """Tim walks faster than normal, randomly, drawing thicker lines and changing colors"""
    tim.pensize(10)
    tim.speed(10)
    for _ in range(steps):
        tim.color(random.choice(COLORS))
        tim.setheading(random.choice(DIRECTIONS))
        tim.forward(20)


# draw_square()
# draw_dashed_line()
# draw_shape(5)
# draw_many_polygons()
# random_walk(200)
screen = Screen()
screen.exitonclick()
