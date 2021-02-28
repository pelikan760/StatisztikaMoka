from tkinter import *
import os

global version 
version = "v0.1.0b"

root = Tk()
root.wm_title(f"Statisztika Móka {version}")
menu = Menu(root)
root.config(menu=menu)
root.iconbitmap(r"C:\Users\Lenovo\Desktop\Programozás (1)\StatisztikaMóka\logo.ico")
root.config(bg="grey25")


#újablak funkció
def new_window_about():
    win = Toplevel()
    win.title(f"Index móka {version}")
    win.iconbitmap(r"C:\Users\Lenovo\Desktop\Programozás (1)\StatisztikaMóka\logo.ico")
    label_appnev = Label(win, text=f"                                         Statisztika Móka {version}").grid(row=0, column=0, columnspan=3)
    #A kurva kép nem akar sehogy sem betöltődni...
    #load = Image.open("logo.png")
    #render = ImageTk.PhotoImage(load)
    #logo = PhotoImage(file="logo.png")
    #label_logo = Label(win, image=render).grid(row=1, column=1)
    label_readme = Label(win, text="Bármilyen kérdés, vagy javaslat esetén vedd fel velem\na kapcsolatot az alábbi emailcímen: pelikanvagyok@gmail.com.", padx=20, pady=10).grid(row=2, column=2, columnspan=3)
    label_license = Label(win, text="AGPL-3.0 license", justify=CENTER).grid(row=3, column=3, columnspan=3)

def new_window_viszonyszámok():
    win = Toplevel()
    win.title(f"Statisztika Móka {version}")
    win.iconbitmap(r"C:\Users\Lenovo\Desktop\Programozás (1)\StatisztikaMóka\logo.ico")

def new_window_átlagok():
    win = Toplevel()
    win.title(f"Statisztika Móka {version}")
    win.iconbitmap(r"C:\Users\Lenovo\Desktop\Programozás (1)\StatisztikaMóka\logo.ico")

def new_window_calc():
    win = Toplevel()
    win.title(f"Statisztika Móka {version}")
    win.iconbitmap(r"C:\Users\Lenovo\Desktop\Programozás (1)\StatisztikaMóka\logo.ico")
    
    e = Entry(win, width=35, borderwidth=5,  bg="gray60")
    e.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

    #main functions
    def button_click(number):
        #e.delete(0, END)
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

    def button_clear():
        e.delete(0, END)

    def button_equal():
        second_number = e.get()
        e.delete(0, END)
    
        if(math == "multi"):
            e.insert(0, f_num * int(second_number))
    
        if(math == "add"):
            e.insert(0, f_num + int(second_number))
    
        if(math == "sub"):
            e.insert(0, f_num - int(second_number))
    
        if(math == "div"):
                e.insert(0, f_num / int(second_number))

    def button_multiply():
        first_num = e.get()
        global f_num
        global math 
        math = "multi"
        f_num = int(first_num)
        e.delete(0, END)

    def button_add():
        first_num = e.get()
        global f_num
        global math 
        math = "add"
        f_num = int(first_num)
        e.delete(0, END)

    def button_subtract():
        first_num = e.get()
        global f_num
        global math 
        math = "sub"
        f_num = int(first_num)
        e.delete(0, END)

    def button_divide():
        first_num = e.get()
        global f_num
        global math 
        math = "div"
        f_num = int(first_num)
        e.delete(0, END)

    #define the buttons
    button_1 = Button(win, text="1", padx=40, pady=20, bg="gray60", fg="DarkOrange4", command=lambda: button_click(1))
    button_2 = Button(win, text="2", padx=40, pady=20, bg="gray60", fg="DarkOrange4", command=lambda: button_click(2))
    button_3 = Button(win, text="3", padx=40, pady=20, bg="gray60", fg="DarkOrange4", command=lambda: button_click(3))
    button_4 = Button(win, text="4", padx=40, pady=20, bg="gray60", fg="DarkOrange4", command=lambda: button_click(4))
    button_5 = Button(win, text="5", padx=40, pady=20, bg="gray60", fg="DarkOrange4", command=lambda: button_click(5))
    button_6 = Button(win, text="6", padx=40, pady=20, bg="gray60", fg="DarkOrange4", command=lambda: button_click(6))
    button_7 = Button(win, text="7", padx=40, pady=20, bg="gray60", fg="DarkOrange4", command=lambda: button_click(7))
    button_8 = Button(win, text="8", padx=40, pady=20, bg="gray60", fg="DarkOrange4", command=lambda: button_click(8))
    button_9 = Button(win, text="9", padx=40, pady=20, bg="gray60", fg="DarkOrange4", command=lambda: button_click(9))
    button_0 = Button(win, text="0", padx=40, pady=20, bg="gray60", fg="DarkOrange4", command=lambda: button_click(0))

    button_multy = Button(win, text="*", padx=41, pady=20, bg="gray60", fg="DarkOrange4", command=button_multiply)
    button_clear = Button(win, text=" clear", padx=77, pady=20, bg="gray60", fg="DarkOrange4", command=button_clear)
    button_equal = Button(win, text="=", padx=87, pady=20, bg="gray60", fg="DarkOrange4", command=button_equal)

    button_subtract = Button(win, text="-", padx=40, pady=20, bg="gray60", fg="DarkOrange4", command=button_subtract)
    button_add = Button(win, text="+", padx=40, pady=20, bg="gray60", fg="DarkOrange4", command=button_add)
    button_divide = Button(win, text=" /", padx=40, pady=20, bg="gray60", fg="DarkOrange4", command=button_divide)

    #place the buttons
    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0)
    button_multy.grid(row=5, column=0)
    button_clear.grid(row=5, column=1, columnspan=2)
    button_equal.grid(row=6, column=1, columnspan=2)

    button_add.grid(row=6, column=0)
    button_subtract.grid(row=4, column=1)
    button_divide.grid(row=4, column=2)

#törlés funkció
def button_clear():
    canvas_levezetes = Canvas(root, width=600, height=250, bg="White")
    canvas_levezetes.grid(row=8, column=1, columnspan=6)
    levezet = Label(canvas_levezetes, padx=300, pady=150)
    levezet.grid(row=8, column=1)
    levezet.destroy()

#fő számítási funkció
def button_induljunk():
    canvas_levezetes = Canvas(root, width=600, height=250, bg="grey60")
    canvas_levezetes.grid(row=8, column=1, columnspan=6)

    q0a = int(e_q0a.get())
    p0a = int(e_p0a.get())
    q0b = int(e_q0b.get())
    p0b = int(e_p0b.get())

    q1a = int(e_q1a.get())
    p1a = int(e_p1a.get())
    q1b = int(e_q1b.get())
    p1b = int(e_p1b.get())
    
    
    if(math == "iv"):
        megoldás_a = (q1a * p1a) / (q0a * p0a)
        megoldás_b = (q1b * p1b) / (q0b * p0b)

        levezet = Label(canvas_levezetes, text=f"iv(egyedi értékindex) : A = {megoldás_a} \n B = {megoldás_b}." , padx=300, pady=150, bg="grey60")
        levezet.grid(row=8, column=1)
    
    if(math == "ip"):
        megoldás_a = p1a / p0a
        megoldás_b = p1b / p0b

        levezet = Label(canvas_levezetes, text=f"ip(egyedi árindex) = A: {megoldás_a} \n B: {megoldás_b}." , padx=300, pady=150, bg="grey60")
        levezet.grid(row=8, column=1)

    if(math == "iq"):
        megoldás_a = q1a / q0a
        megoldás_b = q1b / q0b

        levezet = Label(canvas_levezetes, text=f"iq(egyedi volumenindex) = A: {megoldás_a} \n B: {megoldás_b}." , padx=300, pady=150, bg="grey60")
        levezet.grid(row=8, column=1)
    
    if(math == "Iv"):
        megoldás = (q1a * p1a + q1b * p1b) / (q0a * p0a + q0b * p0b)

        levezet = Label(canvas_levezetes, text=f"Iv(együttes értékindex) = {megoldás}" , padx=300, pady=150, bg="grey60")
        levezet.grid(row=8, column=1)
    
    if(math == "Ip"):
        megoldás = (q1a * p1a + q1b * p1b) / (q1a * p0a + q1b * p0b)

        levezet = Label(canvas_levezetes, text=f"Ip(együttes árindex) = {megoldás}" , padx=300, pady=150, bg="grey60")
        levezet.grid(row=8, column=1)
    
    if(math == "Iq"):
        megoldás = (q1a * p0a + q1b * p0b) / (q0a * p0a + q0b * p0b)

        levezet = Label(canvas_levezetes, text=f"Iq(együttes volumenindex) = {megoldás}" , padx=300, pady=150, bg="grey60")
        levezet.grid(row=8, column=1)

#rádiógombok globalizálása
def radio_iv():
    global math
    math = "iv"

def radio_ip():
    global math
    math = "ip"

def radio_iq():
    global math
    math = "iq"

def radio_Iv():
    global math
    math = "Iv"

def radio_Ip():
    global math
    math = "Ip"

def radio_Iq():
    global math
    math = "Iq"

#menu
funkcio_menu = Menu(menu)
menu.add_cascade(label="Funkciók", menu=funkcio_menu)
funkcio_menu.add_command(label="Indexek")
funkcio_menu.add_command(label="Viszonyszámok", command=new_window_viszonyszámok, state=DISABLED)
funkcio_menu.add_command(label="Középértékek, átlagok", command=new_window_átlagok, state=DISABLED)
funkcio_menu.add_command(label="Számológép", command=new_window_calc)

beallitasok_menu = Menu(menu)
menu.add_cascade(label="Beállítások", menu=beallitasok_menu)
beallitasok_menu.add_command(label="Beállítások", state=DISABLED)
beallitasok_menu.add_command(label="Wiki", state=DISABLED) 
beallitasok_menu.add_command(label="About", command=new_window_about)

#checkboxok
iv = Radiobutton(root, text="iv(egyedi érték)", value="A", command=radio_iv, bg="gray60", fg="DarkOrange4")
ip = Radiobutton(root, text="ip(egyedi ár)", value="B", command=radio_ip, bg="gray60", fg="DarkOrange4")
iq = Radiobutton(root, text="iq(egyedi volumen)", value="C", command=radio_iq, bg="gray60", fg="DarkOrange4")

Iv = Radiobutton(root, text="Iv(együttes érték)", value="D", command=radio_Iv, bg="gray60", fg="DarkOrange4")
Ip = Radiobutton(root, text="Ip(együttes ár)", value="E", command=radio_Ip, bg="gray60", fg="DarkOrange4")
Iq = Radiobutton(root, text="Iq(együttes volumen)", value="F", command=radio_Iq, bg="gray60", fg="DarkOrange4")

#gombok, widgetek definiálása
label_x = Label(root, padx=30, pady=20, bg="gray25")
label_a_termek = Label(root, text="A termék", padx=140, pady=5, bg="grey60", fg="DarkOrange4")
label_b_termek = Label(root, text="B termék", padx=140, pady=5, bg="grey60", fg="DarkOrange4")
label_mennyisegA = Label(root, text="Mennyiség(q)", padx=35, pady=10, bg="grey60", fg="DarkOrange4")
label_mennyisegB = Label(root, text="Mennyiség(q)", padx=35, pady=10, bg="grey60", fg="DarkOrange4")
label_egysegarA = Label(root, text="Egységár(p) ", padx=40, pady=10, bg="grey60", fg="DarkOrange4")
label_egysegarB = Label(root, text="Egységár(p)", padx=40, pady=10, bg="grey60", fg="DarkOrange4")
label_bazisido = Label(root, text="Bázisidőszak(0) ", padx=32, pady=20, bg="grey60", fg="DarkOrange4")
label_targyido = Label(root, text="Tárgyidőszak(1)", padx=32, pady=20, bg="grey60", fg="DarkOrange4")
label_mitszam = Label(root, text="Mit számoljunk?", padx=30, pady=20, bg="grey60", fg="DarkOrange4")
label_levezetes = Label(root, text="Levezetés, megoldás:", padx=30, pady=15, bg="grey60", fg="DarkOrange4")

button_induljunk = Button(root, text="Induljunk", padx=50, pady=20, command=button_induljunk, bg="grey60")
button_clear = Button(root, text="Törlés", padx=60, pady=20, command=button_clear, bg="grey60")

e_q0a = Entry(root, width=30, bg="grey60")
e_p0a = Entry(root, width=30, bg="grey60")
e_q0b = Entry(root, width=30, bg="grey60")
e_p0b = Entry(root, width=30, bg="grey60")

e_q1a = Entry(root, width=30, bg="grey60")
e_p1a = Entry(root, width=30, bg="grey60")
e_q1b = Entry(root, width=30, bg="grey60")
e_p1b = Entry(root, width=30, bg="grey60")

#gombok, widgetek elhelyezése
label_x.grid(row=1, column=1, rowspan=2)
label_a_termek.grid(row=1, column=2, columnspan=2)
label_b_termek.grid(row=1, column=4, columnspan=2)
label_mennyisegA.grid(row=2, column=2)
label_egysegarA.grid(row=2, column=3)
label_mennyisegB.grid(row=2, column=4)
label_egysegarB.grid(row=2, column=5)
label_bazisido.grid(row=3, column=1)
label_targyido.grid(row=4, column=1)
label_mitszam.grid(row=5, column=1)
label_levezetes.grid(row=6, column=1, rowspan=2)

e_q0a.grid(row=3, column=2)
e_p0a.grid(row=3, column=3)
e_q0b.grid(row=3, column=4)
e_p0b.grid(row=3, column=5)

e_q1a.grid(row=4, column=2)
e_p1a.grid(row=4, column=3)
e_q1b.grid(row=4, column=4)
e_p1b.grid(row=4, column=5)

iv.grid(row=5, column=2)
ip.grid(row=5, column=3)
iq.grid(row=5, column=4)

Iv.grid(row=6, column=2)
Ip.grid(row=6, column=3)
Iq.grid(row=6, column=4)

button_induljunk.grid(row=5, column=5, rowspan=2)
button_clear.grid(row=7, column=5)

canvas_levezetes = Canvas(root, width=600, height=250, bg="gray60")
canvas_levezetes.grid(row=8, column=1, columnspan=6)

root.mainloop()