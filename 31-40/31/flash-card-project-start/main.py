import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT = "31-40/31/flash-card-project-start/images/card_front.png"
CARD_BACK = "31-40/31/flash-card-project-start/images/card_back.png"
CARD_RIGHT = "31-40/31/flash-card-project-start/images/right.png"
CARD_WRONG = "31-40/31/flash-card-project-start/images/wrong.png"
FONT_NAME = "Ariel"
current_card = {}

# -------------------------- Language Data --------------------------------- #

try:
    language_data = pandas.read_csv(
        "31-40/31/flash-card-project-start/data/words_to_learn.csv"
    )
except FileNotFoundError:
    language_data = pandas.read_csv(
        "31-40/31/flash-card-project-start/data/french_words.csv"
    )
    WORDS_TO_LEARN = pandas.DataFrame.to_dict(
        language_data,
        orient="records"  # changes the shape of the data to be a list of dicts
    )
else:
    WORDS_TO_LEARN = pandas.DataFrame.to_dict(
        language_data,
        orient="records"  # changes the shape of the data to be a list of dicts
    )


def get_word_and_change_text():
    """Gets a random word, and changes the global current card to that dict, and start_countdown"""
    global current_card
    current_card = random.choice(WORDS_TO_LEARN)

    card_canvas.itemconfig(
        language_text, text="French", fill="black"
    )
    card_canvas.itemconfig(
        word_text, text=current_card["French"], fill="black"
    )
    card_canvas.itemconfig(card_background, image=card_front)
    start_countdown()


def is_known():
    """Removes current card from WORDS_TO_LEARN, then calls get_word_and_change_text"""
    WORDS_TO_LEARN.remove(current_card)

    data = pandas.DataFrame(WORDS_TO_LEARN)
    data.to_csv(
        "31-40/31/flash-card-project-start/data/words_to_learn.csv",
        index=False  # won't add index numbers to the csv
    )

    get_word_and_change_text()


# --------------------------Card Flip and Timer ----------------------------- #


def start_countdown():
    """Calls countdown_to_flip"""
    countdown_to_flip(3)


def countdown_to_flip(count):
    """Counts down timer to flip card"""
    if count > 0:
        window.after(1000, countdown_to_flip, count - 1)
    else:
        flip_card()


def flip_card():
    """Flips the Card background and text"""

    card_canvas.itemconfig(
        language_text,
        text="English",
        fill="white"
    )

    card_canvas.itemconfig(
        word_text,
        text=current_card["English"],
        fill="white"
    )

    card_canvas.itemconfig(card_background, image=card_back)


# ------------------------------------- UI -------------------------------- #
window = tkinter.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card
card_canvas = tkinter.Canvas(
    width=800,
    height=526,
    bg=BACKGROUND_COLOR,
    highlightthickness=0
)
card_front = tkinter.PhotoImage(file=CARD_FRONT)
card_back = tkinter.PhotoImage(file=CARD_BACK)
card_background = card_canvas.create_image(
    400,  # x = half of canvas width
    263,  # y = half of canvas height
    image=card_front
)
# Card Text
language_text = card_canvas.create_text(
    400,
    150,
    text="Title",
    fill="black",
    font=(FONT_NAME, 40, "italic")
)
word_text = card_canvas.create_text(
    400,
    263,
    text="word",
    fill="black",
    font=(FONT_NAME, 60, "bold")
)
card_canvas.grid(column=0, row=0, columnspan=2)

# Wrong Button
image_wrong = tkinter.PhotoImage(file=CARD_WRONG)
wrong_button = tkinter.Button(
    image=image_wrong,
    highlightthickness=0,
    command=get_word_and_change_text
)
wrong_button.grid(column=0, row=1)

# Right Button
image_right = tkinter.PhotoImage(file=CARD_RIGHT)
right_button = tkinter.Button(
    image=image_right,
    highlightthickness=0,
    command=is_known
)
right_button.grid(column=1, row=1)


get_word_and_change_text()

window.mainloop()
