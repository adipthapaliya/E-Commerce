from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox
import subprocess

root=Tk()
root.title('Register')
root.geometry('400x580')
root.resizable(False, False)

#==============================================Database=============================================================


conn=sqlite3.connect('register.db')

c=conn.cursor()

#######table

# c.execute(""" CREATE TABLE login(
        
#         name String NOT NULL,
#         username String PRIMARY KEY,
#         adress String NOT NULL,
#         phoneno Integer NOT NULL,
#         password String NOT NULL,


#         )""")
def run_register():
   root.destroy()
   subprocess.call(["python","register.py"])



def run_login():
    root.destroy()
    subprocess.call(["python","login.py"])


def register():
    
    conn=sqlite3.connect('register.db')

    c=conn.cursor()

    c.execute('SELECT 1 FROM login WHERE username = ?',(usernameR_entry.get(),))

    while len(c.fetchall()) > 0:

        messagebox.showerror("Error","Username already exists")
        
        run_register()

        c.execute('SELECT 1 FROM login WHERE username = ?',(usernameR_entry.get(),))


    c.execute("INSERT INTO login VALUES(:name, :username, :adress, :phoneno, :password, :product_list)",
        
                {
                    "name": name_entry.get(),
                    "username": usernameR_entry.get(),
                    "adress": adress_entry.get(),
                    "phoneno": phoneno_entry.get(),
                    "password": password_entry.get(),
                    
                }
        
        )
    
    messagebox.showinfo("register","register sucessfully")
    
    name_entry.delete(0,END)
    usernameR_entry.delete(0,END)
    adress_entry.delete(0,END)
    phoneno_entry.delete(0,END)
    password_entry.delete(0,END)

    conn.commit()
    conn.close()
    
    run_login()






#=============================================== GUI Of Login page =================================================================

#===========Image=======



facebook=Image.open("Login/facebook.png")
google=Image.open("Login/google.png")
apple=Image.open("Login/apple.png")
signupimage=Image.open("Login/signup.png")

facebook=facebook.resize((190,40),Image.ANTIALIAS)
google=google.resize((190,40),Image.ANTIALIAS)
apple=apple.resize((190,40),Image.ANTIALIAS)
signupimage=signupimage.resize((260,50),Image.ANTIALIAS)

facebook_img=ImageTk.PhotoImage(facebook)
google_img=ImageTk.PhotoImage(google)
twitter_img=ImageTk.PhotoImage(apple)
signup_img=ImageTk.PhotoImage(signupimage)

#======Login text


register_text_label=Label(root,text="CREATE ACCOUNT",font=(Canvas,25))
register_text_label.place(x=55,y=15)

facebook_button=Button(root,image=facebook_img,borderwidth=0)
facebook_button.place(x=100,y=65)
google_button=Button(root,image=google_img,borderwidth=0)
google_button.place(x=100,y=110)
twitter_button=Button(root,image=twitter_img,borderwidth=0)
twitter_button.place(x=100,y=155)

or_useemail_label=Label(root,text="or use email for registration")
or_useemail_label.place(x=120,y=220)

name_label=Label(root,text="Name",font=(Canvas,12))
name_label.place(x=4,y=250)
name_entry=Entry(root,font=Canvas,bg="#E1D9D1",width=35)
name_entry.place(x=4,y=275)

usernameR_label=Label(root,text="Username",font=(Canvas,12))
usernameR_label.place(x=4,y=305)
usernameR_entry=Entry(root,font=Canvas,bg="#E1D9D1",width=35)
usernameR_entry.place(x=4,y=330)

adress_label=Label(root,text="Adress",font=(Canvas,12))
adress_label.place(x=4,y=360)
adress_entry=Entry(root,font=Canvas,bg="#E1D9D1",width=35)
adress_entry.place(x=4,y=385)

phoneno_label=Label(root,text="Phone no",font=(Canvas,12))
phoneno_label.place(x=4,y=415)
phoneno_entry=Entry(root,font=Canvas,bg="#E1D9D1",width=35)
phoneno_entry.place(x=4,y=440)

password_label=Label(root,text="Password",font=(Canvas,12))
password_label.place(x=4,y=470)
password_entry=Entry(root,font=Canvas,bg="#E1D9D1",width=35)
password_entry.place(x=4,y=495)


register_button=Button(root,image=signup_img,borderwidth=0,command=register)
register_button.place(x=80,y=530)






conn.commit()
conn.close()

root.mainloop()