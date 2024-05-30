import tkinter

# instance
window = tkinter.Tk()
window.title("First GUI Program")
# window will scale to size of the stuff inside, but a minsize will help if there is nothing there
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label component
# first needs to be created
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# then place it on the screen; pack takes in a bunch of optional arguments

# data can be changed like accessing a dict
my_label["text"] = "New Text"
# or via config
my_label.config(text="Nueva Texto")

# could use place instead of pack to give coords where top left is 0, 0
# my_label.place(x=100, y=100)

# or even use grid instead of pack and place to work with columns and rows
# The grid is relative to other components
# Grid and pack are mutually exclusive
# my_label.grid(column=0, row=0)

# my_label.pack()


# Button Component
def button_clicked():
    """Clicked"""
    new_text = input_field.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()


# Entry Component
input_field = tkinter.Entry(width=10)
input_field.get()  # This is how to get a hold of the info in the field
input_field.pack()

# keeps the window from closing; needs to be at the end
