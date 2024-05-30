import math
import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    """Stops timer and resets labels and reps"""
    window.after_cancel(timer)
    # how canvas need to be changed
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")
    global reps
    reps = 0
# -------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    """Starts countdown"""
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    """Counts down 1 from input timer"""
    global reps
    minutes = count // 60  # division that discards remainder
    seconds = count % 60  # gets the remainder
    if seconds < 10:
        seconds = f"0{seconds}"  # dynamic typing baby
    canvas.itemconfig(  # this is how canvas's want to be changed
        timer_text, text=f"{minutes}:{seconds}"
    )
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()  # restarts timer

        # adds checkmars
        work_sessions = math.floor(reps / 2)
        checkmarks = ""
        for _ in range(work_sessions):
            checkmarks += "✔"
            checkmark_label.config(text=checkmarks)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label with fg
timer_label = tkinter.Label(
    text="Timer",
    fg=GREEN,
    bg=YELLOW,
    font=(FONT_NAME, 28, "bold")
)
timer_label.grid(column=2, row=1)

# Start Button
start_btn = tkinter.Button(
    text="Start",
    highlightthickness=0,
    command=start_timer
)
start_btn.grid(column=1, row=3)

# Reset Button
reset_btn = tkinter.Button(
    text="Reset",
    highlightthickness=0,
    command=reset_timer
)
reset_btn.grid(column=3, row=3)

# Checkmark label
checkmark_label = tkinter.Label(
    fg=GREEN,
    bg=YELLOW,
    font=(FONT_NAME, 24, "bold")
)
checkmark_label.grid(column=2, row=4)


canvas = tkinter.Canvas(
    width=200,  # based on size of tomato.png
    height=224,  # based on size of tomato.png
    bg=YELLOW,
    highlightthickness=0  # gets rid of border outline
)
tomato_img = tkinter.PhotoImage(file="21-30/28/pomodoro-start/tomato.png")
canvas.create_image(100, 112, image=tomato_img)  # image must be PhotoImage
timer_text = canvas.create_text(
    102,  # x
    130,  # y
    text="00:00",
    fill="white",
    font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=2, row=2)

window.mainloop()
