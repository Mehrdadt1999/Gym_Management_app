from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def war_window(text):
    war = Toplevel()
    war.iconbitmap('eagle.ico')
    war.geometry('320x100')
    war_image = ImageTk.PhotoImage(Image.open('warning.png'))
    image_lbl = Label(war, image=war_image)
    image_lbl.image = war_image
    image_lbl.pack()
    text_label = Label(war, text=text, font=("B Nazanin", 12, "bold"))
    text_label.pack()

def show_info_message(title, message):
    messagebox.showinfo(title=title, message=message)