from tkinter import *
from tkinter import ttk

def átl():
    root = Tk()
    global version 
    version = "v0.2.0"
    global logo
    logo = "logo.ico"
    
    root.geometry("770x400")
    root.iconbitmap(logo)
    root.config(bg="grey25")
    root.wm_title(f"Statisztika Móka {version}")

    vlist = ["3 szám", "4 szám", "5 szám", "6 szám", "7 szám", "8 szám", "9 szám"]

    label = Label(root, text="Átlagolandó számok, művelet:", padx=25, bg="grey60").grid(row=0, column=0, rowspan=2)
    combo = ttk.Combobox(root, values=vlist, state="READONLY", width=23)
    combo.set("Hány számot átlagoljunk?")
    combo.grid(row=2, column=0)
    e0 =  Entry(root, selectborderwidth=3, bg="grey60")
    e1 =  Entry(root, selectborderwidth=3, bg="grey60")
    e2 =  Entry(root, selectborderwidth=3, bg="grey60")
    e3 =  Entry(root, selectborderwidth=3, bg="grey60")
    e4 =  Entry(root, selectborderwidth=3, bg="grey60")
    e5 =  Entry(root, selectborderwidth=3, bg="grey60")
    e6 =  Entry(root, selectborderwidth=3, bg="grey60")
    e7 =  Entry(root, selectborderwidth=3, bg="grey60")
    e8 =  Entry(root, selectborderwidth=3, bg="grey60")

    s0 =  Entry(root, selectborderwidth=3, bg="grey60")
    s1 =  Entry(root, selectborderwidth=3, bg="grey60")
    s2 =  Entry(root, selectborderwidth=3, bg="grey60")
    s3 =  Entry(root, selectborderwidth=3, bg="grey60")
    s4 =  Entry(root, selectborderwidth=3, bg="grey60")
    s5 =  Entry(root, selectborderwidth=3, bg="grey60")
    s6 =  Entry(root, selectborderwidth=3, bg="grey60")
    s7 =  Entry(root, selectborderwidth=3, bg="grey60")
    s8 =  Entry(root, selectborderwidth=3, bg="grey60")


    def retrieve_option():
        option = combo.get()
        if option == "3 szám":
            global össz_e
            össz_e = 3
            e0.grid(row=0, column=3)
            e1.grid(row=1, column=3)
            e2.grid(row=2, column=3)
            e3.grid_forget()
            e4.grid_forget()
            e5.grid_forget()
            e6.grid_forget()
            e7.grid_forget()
            e8.grid_forget()

        if option == "4 szám":
            össz_e = 4
            e0.grid(row=0, column=3)
            e1.grid(row=1, column=3)
            e2.grid(row=2, column=3)
            e3.grid(row=3, column=3)
            e4.grid_forget()
            e5.grid_forget()
            e6.grid_forget()
            e7.grid_forget()
            e8.grid_forget()
        
        if option == "5 szám":
            össz_e = 5
            e0.grid(row=0, column=3)
            e1.grid(row=1, column=3)
            e2.grid(row=2, column=3)
            e3.grid(row=3, column=3)
            e4.grid(row=4, column=3)
            e5.grid_forget()
            e6.grid_forget()
            e7.grid_forget()
            e8.grid_forget()

        if option == "6 szám":
            össz_e = 6
            e0.grid(row=0, column=3)
            e1.grid(row=1, column=3)
            e2.grid(row=2, column=3)
            e3.grid(row=3, column=3)
            e4.grid(row=4, column=3)
            e5.grid(row=5, column=3)
            e6.grid_forget()
            e7.grid_forget()
            e8.grid_forget()

        if option == "7 szám":
            össz_e = 7
            e0.grid(row=0, column=3)
            e1.grid(row=1, column=3)
            e2.grid(row=2, column=3)
            e3.grid(row=3, column=3)
            e4.grid(row=4, column=3)
            e5.grid(row=5, column=3)
            e6.grid(row=6, column=3)
            e7.grid_forget()
            e8.grid_forget()

        if option == "8 szám":
            össz_e = 8
            e0.grid(row=0, column=3)
            e1.grid(row=1, column=3)
            e2.grid(row=2, column=3)
            e3.grid(row=3, column=3)
            e4.grid(row=4, column=3)
            e5.grid(row=5, column=3)
            e6.grid(row=6, column=3)
            e7.grid(row=7, column=3)
            e8.grid_forget()

        if option == "9 szám":
            össz_e = 9
            e0.grid(row=0, column=3)
            e1.grid(row=1, column=3)
            e2.grid(row=2, column=3)
            e3.grid(row=3, column=3)
            e4.grid(row=4, column=3)
            e5.grid(row=5, column=3)
            e6.grid(row=6, column=3)
            e7.grid(row=7, column=3)
            e8.grid(row=8, column=3)

    def retrieve_súly():
        option = combo.get()
        if option == "3 szám":
            global össz_s
            össz_s = 3
            s0.grid(row=0, column=4)
            s1.grid(row=1, column=4)
            s2.grid(row=2, column=4)
            s3.grid_forget()
            s4.grid_forget()
            s5.grid_forget()
            s6.grid_forget()
            s7.grid_forget()
            s8.grid_forget()
        
        if option == "4 szám":
            össz_s = 4
            s0.grid(row=0, column=4)
            s1.grid(row=1, column=4)
            s2.grid(row=2, column=4)
            s3.grid(row=3, column=4)
            s4.grid_forget()
            s5.grid_forget()
            s6.grid_forget()
            s7.grid_forget()
            s8.grid_forget()

        if option == "5 szám":
            össz_s = 5
            s0.grid(row=0, column=4)
            s1.grid(row=1, column=4)
            s2.grid(row=2, column=4)
            s3.grid(row=3, column=4)
            s4.grid(row=4, column=4)
            s5.grid_forget()
            s6.grid_forget()
            s7.grid_forget()
            s8.grid_forget()

        if option == "6 szám":
            össz_s = 6
            s0.grid(row=0, column=4)
            s1.grid(row=1, column=4)
            s2.grid(row=2, column=4)
            s3.grid(row=3, column=4)
            s4.grid(row=4, column=4)
            s5.grid(row=5, column=4)
            s6.grid_forget()
            s7.grid_forget()
            s8.grid_forget()

        if option == "7 szám":
            össz_s = 7
            s0.grid(row=0, column=4)
            s1.grid(row=1, column=4)
            s2.grid(row=2, column=4)
            s3.grid(row=3, column=4)
            s4.grid(row=4, column=4)
            s5.grid(row=5, column=4)
            s6.grid(row=6, column=4)
            s7.grid_forget()
            s8.grid_forget()

        if option == "8 szám":
            össz_s = 8
            s0.grid(row=0, column=4)
            s1.grid(row=1, column=4)
            s2.grid(row=2, column=4)
            s3.grid(row=3, column=4)
            s4.grid(row=4, column=4)
            s5.grid(row=5, column=4)
            s6.grid(row=6, column=4)
            s7.grid(row=7, column=4)
            s8.grid_forget()

        if option == "9 szám":
            össz_s = 9
            s0.grid(row=0, column=4)
            s1.grid(row=1, column=4)
            s2.grid(row=2, column=4)
            s3.grid(row=3, column=4)
            s4.grid(row=4, column=4)
            s5.grid(row=5, column=4)
            s6.grid(row=6, column=4)
            s7.grid(row=7, column=4)
            s8.grid(row=8, column=4)

    def radio_számtani():
        global átlag
        átlag = "számtani"

    def radio_súlySzámtani():
        global átlag
        átlag = "Sszámtani"

    def radio_mértani():
        global átlag
        átlag = "mértani"

    def radio_kronológikus():
        global átlag
        átlag = "kronológikus"

    def átlagolás():
        canvas_levezetes = Canvas(root, bg="grey60", width=300, height=150, ).grid(row=9, column=1, columnspan=2)
        
        if átlag == "számtani" and össz_e == 3:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())

            megoldás = (e00 + e01 + e02) / össz_e
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "számtani" and össz_e == 4:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())

            megoldás = (e00 + e01 + e02 + e03) / össz_e
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "számtani" and össz_e == 5:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            e04 = float(e4.get())

            megoldás = (e00 + e01 + e02 + e03 + e04) / össz_e
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "számtani" and össz_e == 6:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            e04 = float(e4.get())
            e05 = float(e4.get())

            megoldás = (e00 + e01 + e02 + e03 + e04 + e05) / össz_e
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "számtani" and össz_e == 7:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            e04 = float(e4.get())
            e05 = float(e4.get())
            e06 = float(e6.get())

            megoldás = (e00 + e01 + e02 + e03 + e04 + e05 + e06) / össz_e
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "számtani" and össz_e == 8:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            e04 = float(e4.get())
            e05 = float(e4.get())
            e06 = float(e6.get())
            e07 = float(e7.get())

            megoldás = (e00 + e01 + e02 + e03 + e04 + e05 + e06 + e07) / össz_e
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "számtani" and össz_e == 9:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            e04 = float(e4.get())
            e05 = float(e4.get())
            e06 = float(e6.get())
            e07 = float(e7.get())
            e08 = float(e8.get())

            megoldás = (e00 + e01 + e02 + e03 + e04 + e05 + e06 + e07 + e08) / össz_e
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "mértani" and össz_e == 3:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())

            megoldás = (e00 * e01 * e02) ** (1/float(össz_e))
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "mértani" and össz_e == 4:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())

            megoldás = (e00 * e01 * e02 * e03) ** (1/float(össz_e))
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1) 

        if átlag == "mértani" and össz_e == 5:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            e04 = float(e4.get())

            megoldás = (e00 * e01 * e02 * e03 * e04) ** (1/float(össz_e))
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1) 

        if átlag == "mértani" and össz_e == 6:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            e04 = float(e4.get())
            e05 = float(e5.get())

            megoldás = (e00 * e01 * e02 * e03 * e04 * e05) ** (1/float(össz_e))
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1) 

        if átlag == "mértani" and össz_e == 7:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            e04 = float(e4.get())
            e05 = float(e5.get())
            e06 = float(e6.get())

            megoldás = (e00 * e01 * e02 * e03 * e04 * e05 * e06) ** (1/float(össz_e))
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)    
        
        if átlag == "mértani" and össz_e == 8:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            e04 = float(e4.get())
            e05 = float(e5.get())
            e06 = float(e6.get())
            e07 = float(e7.get())

            megoldás = (e00 * e01 * e02 * e03 * e04 * e05 * e06 * e07) ** (1/float(össz_e))
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)     
        
        if átlag == "mértani" and össz_e == 9:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            e04 = float(e4.get())
            e05 = float(e5.get())
            e06 = float(e6.get())
            e07 = float(e7.get())
            e08 = float(e8.get())

            megoldás = (e00 * e01 * e02 * e03 * e04 * e05 * e06 * e07 * e08) ** (1/float(össz_e))
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)  

        if átlag == "kronológikus" and össz_e == 3:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            
            megoldás = ((e00/2) + e01 + (e02/2)) / (össz_e - 1)
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "kronológikus" and össz_e == 4:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            
            megoldás = ((e00/2) + e01 + e02 + (e03/2)) / (össz_e - 1)
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "kronológikus" and össz_e == 5:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            e04 = float(e4.get())
            
            megoldás = ((e00/2) + e01 + e02 +  e03 + (e04/2)) / (össz_e - 1)
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "kronológikus" and össz_e == 6:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            e04 = float(e4.get())
            e05 = float(e5.get())
            
            megoldás = ((e00/2) + e01 + e02 +  e04 + (e05/2)) / (össz_e - 1)
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "kronológikus" and össz_e == 7:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            e04 = float(e4.get())
            e05 = float(e5.get())
            e06 = float(e6.get())
            
            megoldás = ((e00/2) + e01 + e02 +  e04 + e05 + (e06/2)) / (össz_e - 1)
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "kronológikus" and össz_e == 8:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            e04 = float(e4.get())
            e05 = float(e5.get())
            e06 = float(e6.get())
            e07 = float(e7.get())
            
            megoldás = ((e00/2) + e01 + e02 +  e04 + e05 + e06 + (e07/2)) / (össz_e - 1)
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "kronológikus" and össz_e == 9:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            e04 = float(e4.get())
            e05 = float(e5.get())
            e06 = float(e6.get())
            e07 = float(e7.get())
            e08 = float(e8.get())
            
            megoldás = ((e00/2) + e01 + e02 +  e04 + e05 + e06 + e07 + (e08/2)) / (össz_e - 1)
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "Sszámtani" and össz_e == 3:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            
            s00 = float(s0.get())
            s01 = float(s1.get())
            s02 = float(s2.get())

            megoldás = (e00 * s00 + e01 * s01 + e02 * s02) / (s00 + s01 + s02)
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "Sszámtani" and össz_e == 4:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            
            s00 = float(s0.get())
            s01 = float(s1.get())
            s02 = float(s2.get())
            s03 = float(s3.get())

            megoldás = (e00 * s00 + e01 * s01 + e02 * s02 + e03 * s03) / (s00 + s01 + s02 + s03)
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "Sszámtani" and össz_e == 5:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            e04 = float(e4.get())
            
            s00 = float(s0.get())
            s01 = float(s1.get())
            s02 = float(s2.get())
            s03 = float(s3.get())
            s04 = float(s4.get())

            megoldás = (e00 * s00 + e01 * s01 + e02 * s02 + e03 * s03 + e04 * s04) / (s00 + s01 + s02 + s03 + s04)
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "Sszámtani" and össz_e == 6:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            e04 = float(e4.get())
            e05 = float(e5.get())
            
            s00 = float(s0.get())
            s01 = float(s1.get())
            s02 = float(s2.get())
            s03 = float(s3.get())
            s04 = float(s4.get())
            s05 = float(s5.get())

            megoldás = (e00 * s00 + e01 * s01 + e02 * s02 + e03 * s03 + e04 * s04 + e05 * s05) / (s00 + s01 + s02 + s03 + s04 + s05)
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "Sszámtani" and össz_e == 7:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            e04 = float(e4.get())
            e05 = float(e5.get())
            e06 = float(e6.get())
            
            s00 = float(s0.get())
            s01 = float(s1.get())
            s02 = float(s2.get())
            s03 = float(s3.get())
            s04 = float(s4.get())
            s05 = float(s5.get())
            s06 = float(s6.get())

            megoldás = (e00 * s00 + e01 * s01 + e02 * s02 + e03 * s03 + e04 * s04 + e05 * s05 + e06 * s06) / (s00 + s01 + s02 + s03 + s04 + s05 + s06)
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "Sszámtani" and össz_e == 8:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            e04 = float(e4.get())
            e05 = float(e5.get())
            e06 = float(e6.get())
            e07 = float(e7.get())
            
            s00 = float(s0.get())
            s01 = float(s1.get())
            s02 = float(s2.get())
            s03 = float(s3.get())
            s04 = float(s4.get())
            s05 = float(s5.get())
            s06 = float(s6.get())
            s07 = float(s7.get())

            megoldás = (e00 * s00 + e01 * s01 + e02 * s02 + e03 * s03 + e04 * s04 + e05 * s05 + e06 * s06 + e07 * s07) / (s00 + s01 + s02 + s03 + s04 + s05 + s06 + s07)
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)

        if átlag == "Sszámtani" and össz_e == 9:
            e00 = float(e0.get())
            e01 = float(e1.get())
            e02 = float(e2.get())
            e03 = float(e3.get())
            e04 = float(e4.get())
            e05 = float(e5.get())
            e06 = float(e6.get())
            e07 = float(e7.get())
            e08 = float(e8.get())
            
            s00 = float(s0.get())
            s01 = float(s1.get())
            s02 = float(s2.get())
            s03 = float(s3.get())
            s04 = float(s4.get())
            s05 = float(s5.get())
            s06 = float(s6.get())
            s07 = float(s7.get())
            s08 = float(s8.get())

            megoldás = (e00 * s00 + e01 * s01 + e02 * s02 + e03 * s03 + e04 * s04 + e05 * s05 + e06 * s06 + e07 * s07 + e08 * s08) / (s00 + s01 + s02 + s03 + s04 + s05 + s06 + s07 + s08)
            canvas_levezetes = Canvas(root, bg="White", width=300, height=150).grid(row=9, column=1, columnspan=2)
            label_megoldás = Label(canvas_levezetes, text=megoldás).grid(row=9, column=1)


    radio_számtani = Radiobutton(root, text="Számtani átlag       ", justify=LEFT, value="A", command=radio_számtani, bg="grey60").grid(row=0, column=1)
    radio_súlyozott_számtani = Radiobutton(root, text="Súlyozott számtani átlag", justify=LEFT, value="B", command=radio_súlySzámtani, bg="grey60").grid(row=0, column=2)
    radio_mértani = Radiobutton(root, text="Mértani átlag(x.xx)", justify=LEFT, value="C", command=radio_mértani, bg="grey60").grid(row=1, column=1)
    radio_kronológikus = Radiobutton(root, text="Kronológikus átlag          ", justify=LEFT, value="D", command=radio_kronológikus, bg="grey60").grid(row=1, column=2)

    canvas_levezetes = Canvas(root, bg="grey60", width=300, height=150).grid(row=9, column=1, columnspan=2)

    button_szám = Button(root, text="Enter", borderwidth=3, command=retrieve_option, bg="grey60").grid(row=3, column=0)
    button = Button(root, text="Számítás", borderwidth=3, command=átlagolás, bg="grey60").grid(row=2, column=1, columnspan=2)
    button_súly = Button(root, text="Súlyozott", borderwidth=3, command=retrieve_súly, bg="grey60").grid(row=4, column=0)

    
    root.mainloop()
