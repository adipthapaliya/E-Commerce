from tkinter import *
from PIL import Image,ImageTk
import subprocess
import sqlite3
import random
from tkinter import ttk

root=Tk()
root.title("Items")
root.minsize(430,500)
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


        my_canvas.create_window((250,0), window=second_frame)


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



B1 = Image.open("Balls1\B1.jpg")
B2 = Image.open("Balls1\B2.png")
B3 = Image.open("Balls1\B3.jpg")
B4 = Image.open("Balls1\B4.jpg")




B1 = B1.resize((200, 200), Image.ANTIALIAS)
B2 = B2.resize((200, 200), Image.ANTIALIAS)
B3 = B3.resize((200, 200), Image.ANTIALIAS)
B4 = B4.resize((200, 200), Image.ANTIALIAS)



B1 = ImageTk.PhotoImage(B1)
B2 = ImageTk.PhotoImage(B2)
B3 = ImageTk.PhotoImage(B3)
B4 = ImageTk.PhotoImage(B4)




def mainframe():

        global main_frame


                #----------------    Creating a Frame  --------------------------

        main_frame = Frame(root)
        main_frame.place(x=0, y=0)

        my_canvas = Canvas(main_frame, width=400, height=500)
        my_canvas.pack(side=LEFT, fill=BOTH)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, padx=5, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

        second_frame = Frame(my_canvas, width=300, height=500)


        my_canvas.create_window((0, 500), window=second_frame)




                #------------------------   All product Labeling  --------------------------------


        

        b1 = Button(second_frame, image=B1, bg="white", borderwidth=0,command=lambda : description(B1))
        b1.grid(row=1,column=0)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=2,column=0)
        l11=Label(second_frame,text="Wilson Ball")
        l11.grid(row=3,column=0)


        b2 = Button(second_frame, image=B2, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(B2))
        b2.grid(row=1,column=2)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=2,column=2)
        l22=Label(second_frame,text="NBA Ball")
        l22.grid(row=3,column=2)


        b3 = Button(second_frame, image=B3, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(B3))
        b3.grid(row=4,column=0)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=5,column=0)
        l33=Label(second_frame,text="Wilson Leather Ball")
        l33.grid(row=6,column=0)


        b4 = Button(second_frame, image=B4, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(B4))
        b4.grid(row=4,column=2)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=5,column=2)
        l44=Label(second_frame,text="Nike Elite Ball")
        l44.grid(row=6,column=2)


        
       
        


mainframe()









root.mainloop()