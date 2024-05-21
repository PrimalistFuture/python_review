import turtle

# Move timmy the turtle around
tim = turtle.Turtle()
SCREEN = turtle.Screen()


def move_forwards():
    """Tim moves forwards"""
    tim.forward(10)


def move_backwards():
    """Tim moves forwards"""
    tim.back(10)


def turn_left():
    """Tim moves forwards"""
    tim.left(10)


def turn_right():
    """Tim moves forwards"""
    tim.right(10)


def reset():
    """Clears the screen and tim goes back to the middle"""
    tim.reset()


SCREEN.listen()
SCREEN.onkey(key='w', fun=move_forwards)
SCREEN.onkey(key='s', fun=move_backwards)
SCREEN.onkey(key='a', fun=turn_left)
SCREEN.onkey(key='d', fun=turn_right)
SCREEN.onkey(key='c', fun=reset)
SCREEN.exitonclick()
