from tkinter import *
from PIL import Image,ImageTk
import subprocess
import sqlite3
import random
from tkinter import ttk

root=Tk()
root.title("Items")
root.minsize(500,500)
root.resizable(False,False)
root.config(bg="#ffffff")

def details_mainframe(product_image):

        global main_frame

        main_frame = Frame(root)
        main_frame.place(x=0, y=90)

        my_canvas = Canvas(main_frame, width=500, height=500)
        my_canvas.pack(side=LEFT, fill=BOTH)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, padx=5, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

        second_frame = Frame(my_canvas, width=100, height=100)


        my_canvas.create_window((300,0), window=second_frame)


        b1 = Button(second_frame, image=product_image, bg="white", borderwidth=0)
        b1.grid(row=1,column=0)

        add_to_cart=Button(second_frame,text="Add  to cart",bg="black",fg="white")
        add_to_cart.grid(row=3,column=0)
        # lar_ge=Button(second_frame,text="Large",bg="black",fg="white ")
        # lar_ge.grid_info(row=2,column=0)

def description(product_image):
        #============= clear the screen
    for ele in main_frame.winfo_children():
        ele.destroy()

    details_mainframe(product_image)



F1 = Image.open("Dress\F1.jpg")
F2 = Image.open("Dress\F2.jpg")
F3 = Image.open("Dress\F3.png")
F4 = Image.open("Dress\F4.jpg")
F5 = Image.open("Dress\F5.jpg")
F6 = Image.open("Dress\F6.jpg")
F7 = Image.open("Dress\F7.png")
B1 = Image.open("Dress\B1.jpg")
B2 = Image.open("Dress\B2.jpg")


F1 = F1.resize((200, 200), Image.ANTIALIAS)
F2 = F2.resize((200, 200), Image.ANTIALIAS)
F3 = F3.resize((200, 200), Image.ANTIALIAS)
F4 = F4.resize((200, 200), Image.ANTIALIAS)
F5 = F5.resize((200, 200), Image.ANTIALIAS)
F6 = F6.resize((200, 200), Image.ANTIALIAS)
F7 = F7.resize((200, 200), Image.ANTIALIAS)
B1 = B1.resize((200, 200), Image.ANTIALIAS)
B2 = B2.resize((200, 200), Image.ANTIALIAS)

F1 = ImageTk.PhotoImage(F1)
F2 = ImageTk.PhotoImage(F2)
F3 = ImageTk.PhotoImage(F3)
F4 = ImageTk.PhotoImage(F4)
F5 = ImageTk.PhotoImage(F5)
F6 = ImageTk.PhotoImage(F6)
F7 = ImageTk.PhotoImage(F7)
B1 = ImageTk.PhotoImage(B1)
B2= ImageTk.PhotoImage(B2)

def mainframe():

        global main_frame


                #----------------    Creating a Frame  --------------------------

        main_frame = Frame(root)
        main_frame.place(x=0, y=0)

        my_canvas = Canvas(main_frame, width=475, height=500)
        my_canvas.pack(side=LEFT, fill=BOTH)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, padx=5, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

        second_frame = Frame(my_canvas, width=500, height=500)


        my_canvas.create_window((0, 500), window=second_frame)




                #------------------------   All product Labeling  --------------------------------


        

        b1 = Button(second_frame, image=F1, bg="white", borderwidth=0,command=lambda : description(F1))
        b1.grid(row=1,column=0)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=2,column=0)
        l11=Label(second_frame,text="Adidas Real Madrid Jersy(White)")
        l11.grid(row=3,column=0)


        b2 = Button(second_frame, image=F2, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F2))
        b2.grid(row=1,column=1)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=2,column=1)
        l22=Label(second_frame,text="Nike PSG Jersy(Blue)")
        l22.grid(row=3,column=1)


        b3 = Button(second_frame, image=F3, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F3))
        b3.grid(row=4,column=0)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=5,column=0)
        l33=Label(second_frame,text="Jordan Messi PSG Jersy(Blue)")
        l33.grid(row=6,column=0)


        b4 = Button(second_frame, image=F4, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F4))
        b4.grid(row=4,column=1)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=5,column=1)
        l44=Label(second_frame,text="Addidas Manchester United Jersy(Red)")
        l44.grid(row=6,column=1)


        b5 = Button(second_frame, image=F5, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F5))
        b5.grid(row=7,column=0)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=8,column=0)
        l55=Label(second_frame,text="Addidas Modrić Real Madrid Jersy(Pink)")
        l55.grid(row=9,column=0)


        b6 = Button(second_frame, image=F6, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F6))
        b6.grid(row=7,column=1)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=8,column=1)
        l44=Label(second_frame,text="Addidas Bayern Munich Jersy(Red)")
        l44.grid(row=9,column=1)


       
        b9 = Button(second_frame, image=F7, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F7))
        b9.grid(row=10,column=1)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=11,column=1)
        l44=Label(second_frame,text="Adiddas Ronaldo Manchester United Jersy(Red)")
        l44.grid(row=12,column=1)


mainframe()









root.mainloop()