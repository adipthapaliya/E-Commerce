from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox

#============== Main Window ===============

root=Tk()
root.title("LOGIN")
root.geometry('400x580')
root.resizable(FALSE, FALSE)

conn=sqlite3.connect('register.db')

c=conn.cursor()

#######table

# c.execute(""" CREATE TABLE login(
        
#         name String NOT NULL,
#         username String PRIMARY KEY,
#         email String NOT NULL,
#         phoneno Integer NOT NULL,
#         password String NOT NULL

#         )""")

def login():

   conn=sqlite3.connect('register.db')
   c=conn.cursor()

   c.execute('SELECT 1 FROM login WHERE username = ? AND password = ?',(username_entry.get(),password_entry.get()))

   while len(c.fetchall())==0:
      messagebox.showerror("Invalid","Invalid username or password")

      username_entry.delete(0,END)
      password_entry.delete(0,END)

      c.execute('SELECT 1 FROM login WHERE username = ? AND password = ?',(username_entry.get(),password_entry.get()))

   messagebox.showinfo("login","login successfully")




#=============================================== GUI Of Login page =================================================================

#===========Image=======

facebook=Image.open("facebook.png")
google=Image.open("google.png")
apple=Image.open("apple.png")

facebook=facebook.resize((190,40),Image.ANTIALIAS)
google=google.resize((190,40),Image.ANTIALIAS)
apple=apple.resize((190,40),Image.ANTIALIAS)

facebook_img=ImageTk.PhotoImage(facebook)
google_img=ImageTk.PhotoImage(google)
twitter_img=ImageTk.PhotoImage(apple)

#======Login text
login_text_label=Label(root,text="LOGIN",font=(Canvas,30))
login_text_label.place(x=120,y=15)

username_label=Label(root,text="Username",font=(Canvas,12))
username_label.place(x=4,y=90)
username_entry=Entry(root,font=Canvas,bg="#E1D9D1",width=35)
username_entry.place(x=4,y=120)

password_label=Label(root,text="Password",font=(Canvas,12))
password_label.place(x=4,y=150)
password_entry=Entry(root,font=Canvas,bg="#E1D9D1",width=35)
password_entry.place(x=4,y=180)

forget_password_button=Button(root,text="forget password ?",borderwidth=0,fg="green")
forget_password_button.place(x=280,y=220)

login_button=Button(root,text="Login",font=Canvas,command=login)
login_button.place(x=150,y=250)

or_signup_label=Label(root,text="or sigh up using")
or_signup_label.place(x=150,y=310)

facebook_button=Button(root,image=facebook_img,borderwidth=0)
facebook_button.place(x=100,y=330)
google_button=Button(root,image=google_img,borderwidth=0)
google_button.place(x=100,y=375)
twitter_button=Button(root,image=twitter_img,borderwidth=0)
twitter_button.place(x=100,y=420)

or_register_label=Label(root,text="or register using")
or_register_label.place(x=155,y=510)

signup_button=Button(root,text="SIGN UP",font=Canvas)
signup_button.place(x=150,y=535)


conn.commit()
conn.close()
root.mainloop()