import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FALSE_IMG = "31-40/34/quizzler-app-start/images/false.png"
TRUE_IMG = "31-40/34/quizzler-app-start/images/true.png"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    """Quiz interface for Quizzler"""

    # must be of type QuizBrain
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tkinter.Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR
        )
        self.score_label.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(
            width=300,
            height=250,
            bg="white",
            highlightthickness=0
        )
        self.question_text = self.canvas.create_text(
            150,  # xcord
            125,  # ycord
            width=280,  # setting this to less than canvas width above ensures wrapping
            text="",
            fill=THEME_COLOR,
            font=FONT
        )
        self.canvas.grid(
            column=0,
            row=1,
            columnspan=2,
            pady=50
        )

        # True Button
        self.image_true = tkinter.PhotoImage(file=TRUE_IMG)
        self.true_btn = tkinter.Button(
            image=self.image_true,
            highlightthickness=0,
            command=self.true_pressed
        )
        self.true_btn.grid(column=0, row=2)

        # False Button
        self.image_wrong = tkinter.PhotoImage(file=FALSE_IMG)
        self.false_btn = tkinter.Button(
            image=self.image_wrong,
            highlightthickness=0,
            command=self.false_pressed
        )
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Gets the next question from quiz_brain"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score :{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(
                self.question_text,
                text=q_text
            )
        else:
            self.canvas.itemconfig(
                self.question_text,
                text="You have reached the end of the quiz!"
            )
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed(self):
        """Checks to see if the answer to the current question is True"""
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        """Checks to see if the answer to the current question is False"""
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """Changes the background according to if the user got the answer right or wrong"""
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
