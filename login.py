from tkinter import *
from PIL import ImageTk,Image
#============== Main Window ===============

root=Tk()
root.title("LOGIN")
root.geometry('380x530')
root.resizable(FALSE, FALSE)

#=============================================== GUI Of Login page =================================================================

#===========Image=======

facebook=Image.open("facebook.png")
google=Image.open("google.png")
twitter=Image.open("twitter.png")

facebook=facebook.resize((50,50),Image.ANTIALIAS)
google=google.resize((50,50),Image.ANTIALIAS)
twitter=twitter.resize((50,50),Image.ANTIALIAS)

facebook_img=ImageTk.PhotoImage(facebook)
google_img=ImageTk.PhotoImage(google)
twitter_img=ImageTk.PhotoImage(twitter)


#======Login text
login_text_label=Label(root,text="LOGIN",font=(Canvas,30))
login_text_label.grid(row=0,column=2)

username_label=Label(root,text="Username",font=Canvas)
username_label.grid(row=1,column=0)
username_entry=Entry(root,font=Canvas)
username_entry.grid(row=2,column=0)

password_label=Label(root,text="Password",font=Canvas)
password_label.grid(row=3,column=0)
password_entry=Entry(root,font=Canvas)
password_entry.grid(row=4,column=0)

forget_password_button=Button(root,text="forget password ?")
forget_password_button.grid(row=5,column=0)

login_button=Button(root,text="Login",font=Canvas)
login_button.grid(row=6,column=2)

or_signup_label=Label(root,text="or sighup using",font=Canvas)
or_signup_label.grid(row=7,column=2)

facebook_button=Button(root,image=facebook_img)
facebook_button.grid(row=8,column=1)
google_button=Button(root,image=google_img)
google_button.grid(row=8,column=2)
twitter_button=Button(root,image=twitter_img)
twitter_button.grid(row=8,column=3)

or_register_label=Label(root,text="or register using")
or_register_label.grid(row=9,column=0)

signup_button=Button(root,text="SIGN UP",font=Canvas)
signup_button.grid(row=10,column=0)

root.mainloop()