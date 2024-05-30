import tkinter


window = tkinter.Tk()
window.title("Mile to KM Converter")
# window will scale to size of the stuff inside, but a minsize will help if there is nothing there
window.minsize(width=300, height=187)
window.config(padx=20, pady=20)


miles_entry = tkinter.Entry(width=2)
miles_entry.grid(column=2, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=3, row=0)

conversion_label = tkinter.Label(text="is equal to X KM")
conversion_label.grid(column=2, row=1)


def convert():
    """Converts and updates labels"""
    miles = int(miles_entry.get())
    conversion_label["text"] = f"is equal to {miles * 1.6} KM"


calc_button = tkinter.Button(text="Calculate", command=convert)
calc_button.grid(column=2, row=2)

window.mainloop()
