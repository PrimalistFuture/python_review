import tkinter
from tkinter import END, messagebox
import random
import pyperclip

# --------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project from Day 5


def generate_password():
    """Generates password"""
    password_field.delete(0, END)  # clears password field

    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
        'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_field.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    """Gets the data from the fields, calls write_to_txt_file"""

    website = website_field.get()  # gets data from field
    email = email_field.get()
    password = password_field.get()

    # checks for empty fields
    if len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showinfo(
            title="Field Empty",
            message="One or more of the fields is empty."
        )
        return

    # confirmation message
    is_ok = messagebox.askokcancel(
        title=website,
        message=f"""There are the details entered: \n
        Email: {email} \n
        Password: {password} \n
        Is it ok to save?"""
    )
    if is_ok:
        data = f"{website} | {email} | {password} \n"
        write_to_txt_file(data)


def write_to_txt_file(data):
    """Appends the data to txt file, calls clean_entries"""

    path = "21-30/29/password-manager-start/data.txt"
    with open(path, "a", encoding="UTF-8") as file:
        file.write(data)

    clean_entries()


def clean_entries():
    """Deletes text from entry fields"""

    website_field.delete(0, END)
    password_field.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas widgit for image
canvas = tkinter.Canvas(
    width=200,  # based on size of logo.png
    height=200,  # based on size of logo.png
    highlightthickness=0  # gets rid of border outline
)
logo_img = tkinter.PhotoImage(
    file="21-30/29/password-manager-start/logo.png"
)
canvas.create_image(
    100,  # xpos
    100,  # ypos
    image=logo_img  # image must be PhotoImage
)
canvas.grid(column=1, row=0)


# Website Label
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

# Website Entry
website_field = tkinter.Entry(width=35)
website_field.grid(column=1, row=1, columnspan=2, sticky="EW")
website_field.focus()

# Email/Username Label
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

# Email Entry
email_field = tkinter.Entry(width=35)
email_field.grid(column=1, row=2, columnspan=2, sticky="EW")
email_field.insert(0, "my_email@email.com")

# Password Label
password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

# Password Entry
password_field = tkinter.Entry(width=21)
password_field.grid(column=1, row=3, sticky="EW")

# Password Button
password_btn = tkinter.Button(
    text="Generate Password",
    command=generate_password
)
password_btn.grid(column=2, row=3, sticky="EW")

# Add Button
add_btn = tkinter.Button(text="Add", width=36, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
