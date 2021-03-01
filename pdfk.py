from tkinter import *
from PIL import Image,ImageTk

def new_window_képlet():
    global version 
    version = "v0.1.2b"
    global icon
    logo = "logo.ico"
    root1 = Toplevel()
    root1.wm_title(f"Statisztika Móka {version}")
    root1.iconbitmap(logo)

    #canvas = Canvas(root1, width=600, height=600, bg="black").grid(row=0, column=0, columnspan=3, rowspan=2)

    képlet0 = ImageTk.PhotoImage(Image.open("képlet-1.png"))
    label = Label(root1, image=képlet0).grid(row=1, column=1)

    képlet1 = ImageTk.PhotoImage(Image.open("képlet-2.png"))
    label1 = Label(root1, image=képlet1).grid(row=1, column=2)


    root1.mainloop()
