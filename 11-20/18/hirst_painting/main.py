import random
import turtle
# import colorgram

# colors = colorgram.extract('image.jpg', 10)
# print(colors)

turtle.colormode(255)
tim = turtle.Turtle()


def random_color():
    """Generates a random rgb tuple"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_dots(dots):
    """Tim draws a row of dots until input, starting at the bottom left-ish"""
    tim.setheading(225)
    tim.penup()
    tim.forward(300)
    tim.setheading(0)
    tim.speed(0)

    for dot_count in range(1, dots + 1):
        tim.dot(20, random_color())
        tim.penup()
        tim.forward(50)

        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)
    tim.hideturtle()


draw_dots(10)
SCREEN = turtle.Screen()
SCREEN.exitonclick()
