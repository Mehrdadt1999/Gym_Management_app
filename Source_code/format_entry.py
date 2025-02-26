from tkinter import *

# function for make tuition readable
def format_entry(entry):
    value = str(entry.get()).replace(",", "")
    try:
        value = int(value)
        formatted_value = "{:,}".format(value)
        entry.delete(0, END)
        entry.insert(0, formatted_value)
    except ValueError:
        pass