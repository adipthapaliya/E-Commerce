from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title('Register')
root.geometry('400x580')
root.resizable(False, False)


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

email_label=Label(root,text="Email",font=(Canvas,12))
email_label.place(x=4,y=360)
email_entry=Entry(root,font=Canvas,bg="#E1D9D1",width=35)
email_entry.place(x=4,y=385)

phoneno_label=Label(root,text="Phone no",font=(Canvas,12))
phoneno_label.place(x=4,y=415)
phoneno_entry=Entry(root,font=Canvas,bg="#E1D9D1",width=35)
phoneno_entry.place(x=4,y=440)

password_label=Label(root,text="Password",font=(Canvas,12))
password_label.place(x=4,y=470)
password_entry=Entry(root,font=Canvas,bg="#E1D9D1",width=35)
password_entry.place(x=4,y=495)


register_button=Button(root,text="SIGN UP",font=Canvas)
register_button.place(x=150,y=535)














root.mainloop()