'''so,this terminal has a codes that will make a window for main menu and other options'''

from tkinter import *
from PIL import ImageTk,Image





window = Tk()

window.geometry("1000x690")
window.configure(bg ="MAROON")
window.resizable(0,0)

# Following codes helps us to insert images
image1=Image.open("messi.png")
image1=image1.resize((452,452),Image.ANTIALIAS) #this will fit images as size we needed
myimg1=ImageTk.PhotoImage(image1)
mylbl1=Label(image=myimg1)
mylbl1.place(x=0,y=30)

image2=Image.open("s.jpg")
image2=image2.resize((220,226),Image.ANTIALIAS)
myimg2=ImageTk.PhotoImage(image2)
mylbl2=Label(image=myimg2)
mylbl2.place(x=0,y=490)

image3=Image.open("30.jpg")
image3=image3.resize((226,226),Image.ANTIALIAS)
myimg3=ImageTk.PhotoImage(image3)
mylbl3=Label(image=myimg3)
mylbl3.place(x=226,y=490)



label_4 = Label(window, text="S.O.D E-COMMERCE",borderwidth=4,relief=GROOVE,width=20,font=("bold", 15),bg="BROWN",padx=114,pady=3)
label_4.place(x=0,y=0)
#canvas will create a border or line as a seperator on window
mycanvas=Canvas(window,width=452,height=2,bg="black")
mycanvas.place(x=0,y=485)

mycanvas1=Canvas(window,width=556,height=1,bg="blue")
mycanvas1.place(x=456,y=33)

mycanvas2=Canvas(window,width=1,height=1000,bg="blue")
mycanvas2.place(x=452,y=37)

# this code will help us to create menubutton
mb=Menubutton(window,text="MENU",relief=GROOVE,padx=25,pady=8,bg="blue")
mb.place(x=453,y=20)
mb.menu=Menu(mb,tearoff=0,bg="maroon",fg="white")
mb["menu"]=mb.menu
mb.menu.add_command(label="Balls")
mb.menu.add_separator()
mb.menu.add_command(label="Wears")
mb.menu.add_separator()
mb.menu.add_command(label="Report")
mb.menu.add_separator()
mb.menu.add_command(label="exit")
mb.menu.add_separator()
mb.pack()

# mb2 is for submenu
mb1=Menubutton(window,text="MENS",relief=GROOVE,padx=25,pady=8,bg="blue")
mb1.place(x=700,y=0)
mb1.menu=Menu(mb1,tearoff=0,bg="maroon",fg="white")
mb1["menu"]=mb1.menu
mb2=Menu(mb1,tearoff=0,bg="Maroon",fg="yellow")
mb2.add_command(label="Wear")
mb2.add_separator()
mb2.add_command(label="Balls")



mb1.menu.add_cascade(label="Football",menu=mb2)
mb1.menu.add_separator()
mb1.menu.add_cascade(label="Basketball",menu=mb2)
mb1.menu.add_separator()
mb1.menu.add_cascade(label="Cricket",menu=mb2)
mb1.menu.add_separator()
mb1.menu.add_cascade(label="Others") #cascade will make a options box for submenu
mb1.menu.add_separator()

# mb4 is for submenu
mb3=Menubutton(window,text="Womens",relief=GROOVE,padx=25,pady=8,bg="blue") #relief is for frame border design
mb3.place(x=900,y=0)
mb3.menu=Menu(mb3,tearoff=0,bg="maroon",fg="white") #tearoff helps us for dropdown menubuttton
mb3["menu"]=mb3.menu
mb4=Menu(mb3,tearoff=0,bg="Maroon",fg="yellow")
mb4.add_command(label="Wear")
mb4.add_separator() #create lines between dropdown menubutton
mb4.add_command(label="Balls")



mb3.menu.add_cascade(label="Football",menu=mb4)
mb3.menu.add_separator()
mb3.menu.add_cascade(label="Basketball",menu=mb4)
mb3.menu.add_separator()
mb3.menu.add_cascade(label="Cricket",menu=mb4)
mb3.menu.add_separator()
mb3.menu.add_cascade(label="Others")
mb3.menu.add_separator()






window.mainloop()
