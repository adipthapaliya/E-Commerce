
from tkinter import *
from PIL import Image,ImageTk
import subprocess
import sqlite3
import random
from tkinter import ttk
from argparse import ArgumentParser

root=Tk()
root.title("SOD")
# root.attributes("-fullscreen", True)
root.state("zoomed")
root.resizable(False,False)
root.config(bg="#ffffff")

#===============username

parser = ArgumentParser()
parser.add_argument("-u", "--user")

args = vars(parser.parse_args())
user = args['user']


#=====================================Database===========================================================================
conn=sqlite3.connect('register.db')

c=conn.cursor()

        #======================table====================

# c.execute(""" CREATE TABLE login(
        
#         name String NOT NULL,
#         username String PRIMARY KEY,
#         email String NOT NULL,
#         phoneno Integer NOT NULL,
#         password String NOT NULL

#         )""")

def run_login():
    root.destroy()
    subprocess.call(["python","login.py"])

#============================================GUI=============================================================

       #=======================================Images====================================
logo=Image.open("sw.png")
search=Image.open("search.png")
profile=Image.open("profile.png")
contact=Image.open("contact.png")
cart=Image.open("cart.png")




logo=logo.resize((300,50),Image.ANTIALIAS)
search=search.resize((45,35),Image.ANTIALIAS)
profile=profile.resize((30,30),Image.ANTIALIAS)
contact=contact.resize((90,40),Image.ANTIALIAS)
cart=cart.resize((30,30),Image.ANTIALIAS)



logo_img=ImageTk.PhotoImage(logo)
search_img=ImageTk.PhotoImage(search)
profile_img=ImageTk.PhotoImage(profile)
contact_img=ImageTk.PhotoImage(contact)
cart_img=ImageTk.PhotoImage(cart)



        #====================== random offer list===============================================




logo_button=Button(root,image=logo_img,borderwidth=0)
logo_button.place(x=0,y=0)

search_entry=Entry(root,width=91,fg="black",justify="right",borderwidth=2,font="50")
search_entry.place(x=320,y=0,height=50)

search_button=Button(root,image=search_img,borderwidth=0)
search_button.place(x=1160,y=0)

cart_button=Button(root,image=cart_img,borderwidth=0)
cart_button.place(x=1250,y=0)

contact_button=Button(root,image=contact_img,borderwidth=0)
contact_button.place(x=1310,y=0)


        #===============================label of username using database=========================


welcome_label=Label(root,text="WELCOME!")
welcome_label.place(x=1420,y=0)


c.execute('SELECT * FROM login WHERE username = ?',(user,))

records=c.fetchone()
username=records[1]



username_label=Label(root,text=username)
username_label.place(x=1420,y=15)



#=========================================GUI==============================================================================
profile_button=Button(root,image=profile_img,borderwidth=0,command=run_login)
profile_button.place(x=1500,y=0)

                #=======================================Menu  BUttons ====================================

mb1 = Menubutton(root, text="MENS       ▼", relief=GROOVE, padx=25, pady=8, bg="black", fg="white")
mb1.place(x=320, y=50)
mb1.menu = Menu(mb1, tearoff=0, bg="white", fg="black")
mb1["menu"] = mb1.menu
mb2 = Menu(mb1, tearoff=0, bg="white", fg="black")
mb2.add_command(label="Wear", activebackground="black", activeforeground="white")
mb2.add_separator()
mb2.add_command(label="Balls", activebackground="black", activeforeground="white")

mb1.menu.add_cascade(label="Football", menu=mb2, activebackground="black", activeforeground="white")
mb1.menu.add_separator()
mb1.menu.add_cascade(label="Basketball", menu=mb2, activebackground="black", activeforeground="white")

# cascade will make a options box for submenu

mb3 = Menubutton(root, text="WOMENS       ▼", relief=GROOVE, padx=25, pady=8, bg="black", fg="white")
mb3.place(x=450, y=50)
mb3.menu = Menu(mb3, tearoff=0, bg="white", fg="black")
mb3["menu"] = mb3.menu
mb4 = Menu(mb3, tearoff=0, bg="white", fg="black")
mb4.add_command(label="Wear", activebackground="black", activeforeground="white")
mb4.add_separator()
mb4.add_command(label="Balls", activebackground="black", activeforeground="white")

mb3.menu.add_cascade(label="Football", menu=mb4, activebackground="black", activeforeground="white")
mb3.menu.add_separator()
mb3.menu.add_cascade(label="Basketball", menu=mb4, activebackground="black", activeforeground="white")

mb5 = Button(root, text="⚽    Balls    ⚽", relief=GROOVE, padx=25, pady=4, bg="black", fg="white")
mb5.place(x=700, y=50)

mb6 = Button(root, text="⌂ HOME", relief=GROOVE, padx=25, pady=4, bg="black", fg="white", )
mb6.place(x=2, y=52)

            



#======================================Shopping List============================

offer=Image.open("Dress\offer.png")
offer1=Image.open("Dress\offer1.png")


offer=offer.resize((1500,500),Image.ANTIALIAS)
offer1=offer1.resize((1500,500),Image.ANTIALIAS)


offer_img=ImageTk.PhotoImage(offer)
offer1_img=ImageTk.PhotoImage(offer1)

offer_list=[offer_img,offer1_img]




F1 = Image.open("Dress\F1.jpg")
F2 = Image.open("Dress\F2.jpg")
F3 = Image.open("Dress\F3.png")
F4 = Image.open("Dress\F4.jpg")
F5 = Image.open("Dress\F5.jpg")
F6 = Image.open("Dress\F6.jpg")
B1 = Image.open("Dress\B1.jpg")
B2 = Image.open("Dress\B2.jpg")


F1 = F1.resize((400, 400), Image.ANTIALIAS)
F2 = F2.resize((400, 400), Image.ANTIALIAS)
F3 = F3.resize((400, 400), Image.ANTIALIAS)
F4 = F4.resize((400, 400), Image.ANTIALIAS)
F5 = F5.resize((400, 400), Image.ANTIALIAS)
F6 = F6.resize((400, 400), Image.ANTIALIAS)
B1 = B1.resize((400, 400), Image.ANTIALIAS)
B2 = B2.resize((400, 400), Image.ANTIALIAS)

F1 = ImageTk.PhotoImage(F1)
F2 = ImageTk.PhotoImage(F2)
F3 = ImageTk.PhotoImage(F3)
F4 = ImageTk.PhotoImage(F4)
F5 = ImageTk.PhotoImage(F5)
F6 = ImageTk.PhotoImage(F6)
B1 = ImageTk.PhotoImage(B1)
B2= ImageTk.PhotoImage(B2)

                #=============creting a window===============

main_frame = Frame(root)
main_frame.place(x=0, y=90)

my_canvas = Canvas(main_frame, width=1500, height=740)
my_canvas.pack(side=LEFT, fill=BOTH)

my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, padx=5, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

second_frame = Frame(my_canvas, width=1500, height=740)





my_canvas.create_window((0, 0), window=second_frame)

offer_random=random.randint(0,1)
offer_label=Label(second_frame,image=offer_list[offer_random])
offer_label.grid(row=0,column=0,columnspan=3)


b1 = Button(second_frame, image=F1, bg="white", borderwidth=0)
b1.grid(row=1,column=0)
l1=Label(second_frame,text="Rs 1150")
l1.grid(row=2,column=0)
l11=Label(second_frame,text="Adidas Real Madrid Jersy(White)")
l11.grid(row=3,column=0)

b2 = Button(second_frame, image=F2, bg="white", relief=GROOVE,borderwidth=0)
b2.grid(row=1,column=1)
l2=Label(second_frame,text="Rs 1150")
l2.grid(row=2,column=1)
l22=Label(second_frame,text="Nike PSG Jersy(Blue)")
l22.grid(row=3,column=1)

b3 = Button(second_frame, image=F3, bg="white", relief=GROOVE,borderwidth=0)
b3.grid(row=1,column=2)
l2=Label(second_frame,text="Rs 5000")
l2.grid(row=2,column=2)
l22=Label(second_frame,text="Nike Messi PSG Jersy(Blue)")
l22.grid(row=3,column=2)


# b4 = Button(second_frame, image=F4, bg="white", relief=GROOVE,borderwidth=0).grid(row=2,column=0)
# b5 = Button(second_frame, image=F5, bg="white", relief=GROOVE,borderwidth=0).grid(row=2,column=1)
# b6 = Button(second_frame, image=F6, bg="white", relief=GROOVE,borderwidth=0).grid(row=2,column=2)
# b7 = Button(second_frame, image=B1, bg="white", relief=GROOVE,borderwidth=0).grid(row=3,column=0)
# b8 = Button(second_frame, image=B2, bg="white", relief=GROOVE,borderwidth=0).grid(row=3,column=1)


conn.commit()
conn.close()

root.mainloop()