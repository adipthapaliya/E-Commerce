from tkinter import *
from PIL import Image,ImageTk
import subprocess


root=Tk()
root.title("SOD")
# root.attributes("-fullscreen", True)
root.state("zoomed")
root.resizable(False,False)

def run_login():
    root.destroy()
    subprocess.call(["python","login.py"])

#============================================GUI=============================================================
logo=Image.open("sw.png")
search=Image.open("search.png")
profile=Image.open("profile.png")

logo=logo.resize((300,50),Image.ANTIALIAS)
search=search.resize((45,35),Image.ANTIALIAS)
profile=profile.resize((30,30),Image.ANTIALIAS)

logo_img=ImageTk.PhotoImage(logo)
search_img=ImageTk.PhotoImage(search)
profile_img=ImageTk.PhotoImage(profile)


logo_button=Button(root,image=logo_img,borderwidth=0)
logo_button.place(x=0,y=0)

search_entry=Entry(root,width=90,fg="black",justify="right",borderwidth=2,font="50")
search_entry.place(x=320,y=0,height=50)

search_button=Button(root,image=search_img,borderwidth=0)
search_button.place(x=1150,y=0)


profile_button=Button(root,image=profile_img,borderwidth=0,command=run_login)
profile_button.place(x=1500,y=0)


root.mainloop()