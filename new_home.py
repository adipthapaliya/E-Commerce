
from tkinter import *
from PIL import Image,ImageTk
import subprocess
import sqlite3
import random


root=Tk()
root.title("SOD")
# root.attributes("-fullscreen", True)
root.state("zoomed")
root.resizable(False,False)

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

offer=Image.open("offer.png")
offer1=Image.open("offer1.png")


logo=logo.resize((300,50),Image.ANTIALIAS)
search=search.resize((45,35),Image.ANTIALIAS)
profile=profile.resize((30,30),Image.ANTIALIAS)
contact=contact.resize((90,40),Image.ANTIALIAS)
cart=cart.resize((30,30),Image.ANTIALIAS)

offer=offer.resize((1530,500),Image.ANTIALIAS)
offer1=offer1.resize((1530,500),Image.ANTIALIAS)

logo_img=ImageTk.PhotoImage(logo)
search_img=ImageTk.PhotoImage(search)
profile_img=ImageTk.PhotoImage(profile)
contact_img=ImageTk.PhotoImage(contact)
cart_img=ImageTk.PhotoImage(cart)
offer_img=ImageTk.PhotoImage(offer)
offer1_img=ImageTk.PhotoImage(offer1)


        #====================== random offer list===============================================

offer_list=[offer_img,offer1_img]


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


c.execute("SELECT *,oid FROM login")
records=c.fetchone()
username=" "


for i in records:
    username=str(records[1])


username_label=Label(root,text=username)
username_label.place(x=1420,y=15)



#=========================================GUI==============================================================================
profile_button=Button(root,image=profile_img,borderwidth=0,command=run_login)
profile_button.place(x=1500,y=0)


        #==================================Offer images==================

offer_random=random.randint(0,1)
offer_label=Label(root,image=offer_list[offer_random])
offer_label.place(x=0,y=100)


conn.commit()
conn.close()

root.mainloop()