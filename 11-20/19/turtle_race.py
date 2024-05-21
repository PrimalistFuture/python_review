import turtle
import random

# Multiple turtle instances
tim = turtle.Turtle("turtle")
tom = turtle.Turtle("turtle")
tam = turtle.Turtle("turtle")
tum = turtle.Turtle("turtle")
tem = turtle.Turtle("turtle")
tym = turtle.Turtle("turtle")
TURTLES = [tim, tom, tam, tum, tem, tym]

# Screen instance
SCREEN = turtle.Screen()
SCREEN.setup(width=500, height=400)
MAX_HEIGHT = 400
FINISH_LINE = 220


def move_turtle_to_start(t, y_cord):
    """Moves the input turtle to the left of the screen"""
    t.penup()
    t.goto(x=-230, y=y_cord)


def move_all_turtles_to_start_and_give_color(turtle_list):
    """Moves all turtles to the far left of the screen"""
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    idx = 0
    y_cord = -180
    y_increments = (MAX_HEIGHT - 10) / len(turtle_list)

    for tur in turtle_list:
        tur.color(colors[idx])
        idx += 1
        move_turtle_to_start(tur, y_cord)
        y_cord += y_increments


def move_forward(tur, units):
    """Moves input turtle forward input units"""
    tur.forward(units)


def check_for_win(tur):
    """Checks to see if input turtle has crossed finish line"""
    position = tur.position()
    return position[0] > FINISH_LINE


def turtle_race(turtle_list):
    """Conducts the turtles"""
    has_winner = False
    while has_winner is False:
        for tur in turtle_list:
            units_to_move = random.randint(1, 10)
            move_forward(tur, units_to_move)
            did_win = check_for_win(tur)
            if did_win is True:
                has_winner = True
                return (tur, tur.pencolor())


user_bet = SCREEN.textinput(
    title="Make your bet",
    prompt="""Which turtle will win the race? Enter a color: """
).lower()
move_all_turtles_to_start_and_give_color(TURTLES)
winner, winning_color = turtle_race(TURTLES)

print(f"The winner is {winning_color}!")
if winning_color == user_bet:
    print("You won the bet!")
else:
    print("You lost the bet!")
SCREEN.exitonclick()
