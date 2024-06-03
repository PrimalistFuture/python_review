import tkinter
from tkinter import END, messagebox
import random
import pyperclip
import json

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

    data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    write_to_json_file(data)


def write_to_json_file(data):
    """Appends the data to txt file, calls clean_entries"""

    path = "21-30/30/password-manager-start/data.json"
    try:
        with open(path, "r", encoding="UTF-8") as file:
            # reads the old data
            old_data = json.load(file)
            # updates the old data
            old_data.update(data)  # its not sure this is json but it is

    except FileNotFoundError:
        with open(path, "w", encoding="UTF-8") as file:
            json.dump(data, file, indent=4)

    else:
        with open(path, "w", encoding="UTF-8") as file:
            # Saving the updated data
            json.dump(old_data, file, indent=4)

    finally:
        clean_entries()


def clean_entries():
    """Deletes text from entry fields"""

    website_field.delete(0, END)
    password_field.delete(0, END)


# --------------------------- Search ---------------------------------#

def search_data():
    """Searches the data file for a given website"""
    website = website_field.get()  # gets the data from the field
    path = "21-30/30/password-manager-start/data.json"
    try:
        with open(path, "r", encoding="UTF-8") as file:  # poss FNF error
            data = json.load(file)
            website_data = data[website]  # poss KeyError
    except FileNotFoundError:
        fnf_message = messagebox.showinfo(
            title="Website Error",
            message="There are no previous websites to search."
        )
    except KeyError:
        ke_message = messagebox.showinfo(
            title="Website Error",
            message=f"{website} has no saved data."
        )
    else:
        website_message = messagebox.showinfo(
            title="Website Data",
            message=f"{website_data}"
        )


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
    file="21-30/30/password-manager-start/logo.png"
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
website_field = tkinter.Entry(width=21)
website_field.grid(column=1, row=1, columnspan=2, sticky="EW")
website_field.focus()

# Website Search Button
website_search_button = tkinter.Button(
    text="Search",
    command=search_data
)
website_search_button.grid(column=2, row=1, sticky="EW")

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
