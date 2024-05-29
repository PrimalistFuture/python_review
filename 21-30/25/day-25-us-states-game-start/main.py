import turtle
import pandas

# screen instance settings
screen = turtle.Screen()
screen.title("U.S. States Game")
IMAGE = "21-30/25/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)
# screen.bgpic(IMAGE)   #this works too


# turtle instance settings
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)

# Constants
TIMER = 1600
STATES = 50
FONT = ("Courier", 12, "normal")

# pandas data
data = pandas.read_csv(
    "21-30/25/day-25-us-states-game-start/50_states.csv"
)

# Could be used to get coords if they weren't already in the csv
# def get_mouse_click_coor(x,y):
#     """Click on location to get coordinates"""
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()  # keeps the screen open. cant use screen.exitonclick()


def write_state_name(state_name, x, y):
    """Writes the name of the state"""
    pen.goto(x, y)
    pen.write(f"{state_name}", align="center", font=FONT)


def create_missed_states_csv(answered_state_list):
    """Creates an object of the missed states and create a csv of it """
    all_states = data.state.values
    missed_states = []

    for state in all_states:
        if state not in answered_state_list:
            missed_states.append(state)

    # The above could be a comprehension
    # missed_states_comprehension = [
    #     state for state in all_states if state not in answered_state_list]

    missed_states = {
        "state": missed_states
    }

    pd_states_df = pandas.DataFrame(missed_states)
    pd_states_df.to_csv(
        "21-30/25/day-25-us-states-game-start/missed_states.csv"
    )


def states_game():
    """Conducts the states game"""
    correct_states = 0
    answered_states = []

    while correct_states < STATES:
        answer_state = screen.textinput(
            title=f"{correct_states} / {STATES}", prompt="Name a State:"
        ).title()
        # print(data.state.values[28], type(data.state.values[28]))
        if answer_state in data.state.values and answer_state not in answered_states:
            state_data = data[data.state == f"{answer_state}"].values

            write_state_name(
                state_data[0][0],
                state_data[0][1],
                state_data[0][2]
            )

            correct_states += 1
            answered_states.append(answer_state)
        if answer_state == 'Exit':
            create_missed_states_csv(answered_states)
            break


states_game()
