
from tkinter import *
from PIL import Image,ImageTk
import subprocess
import sqlite3
import random
from tkinter import ttk
from argparse import ArgumentParser



#===========================================     Main Window         =========================================================



root=Tk()
root.title("SOD")
# root.attributes("-fullscreen", True)
root.state("zoomed")
root.resizable(False,False)
root.config(bg="#ffffff")



#========================================     ALL Funtions     ============================================================



        #--------------     Login Page   -----------------------------



def run_login():

    root.destroy()
    subprocess.call(["python","login.py"])



        #----------------------     Home page Function   -------------------



def back_home():

    for ele in main_frame.winfo_children():
        ele.destroy()

    mainframe()



        #--------------   Product Details Function ----------------------


             #-------------------       ball product    ----------------------



def ball_details_mainframe(product_image,product_price,product_info):

                #---------------------          funtion to dipaly size       -------------------------


        def size_value(product_size):
                size_display.delete(0,END)
                size_display.insert(0,product_size)


        global main_frame

        main_frame = Frame(root,bg="#ffffff")
        main_frame.place(x=0, y=90)

        my_canvas = Canvas(main_frame, width=1500, height=740,bg="#ffffff")
        my_canvas.pack(side=LEFT, fill=BOTH)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, padx=5, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

        second_frame = Frame(my_canvas, width=1500, height=740,bg="#ffffff")

        my_canvas.create_window((0, 0), window=second_frame)



        passed_image = Label(second_frame, image=product_image, bg="white", borderwidth=0)
        passed_image.grid(row=0,column=0,ipadx=40,ipady=70,rowspan=10)

        passed_image_price=Label(second_frame,text=product_price)
        passed_image_price.grid(row=1,column=1,columnspan=4)

        passed_image_info=Label(second_frame,text=product_info)
        passed_image_info.grid(row=2,column=1,columnspan=4)

        size_label=Label(second_frame,text="Size")
        size_label.grid(row=3,column=1)
        size_display=Entry(second_frame,width=4)
        size_display.grid(row=3,column=2)

        Large=Button(second_frame,text="2",bg="black",fg="white",command=lambda : size_value("2"))
        Large.grid(row=4,column=1)
        Medium=Button(second_frame,text="3",bg="black",fg="white",command=lambda : size_value("3"))
        Medium.grid(row=4,column=2)
        small=Button(second_frame,text="4",bg="black",fg="white",command=lambda : size_value("4"))
        small.grid(row=4,column=3)
        vsmall=Button(second_frame,text="5",bg="black",fg="white",command=lambda : size_value("5"))
        vsmall.grid(row=4,column=4)

        add_to_cart=Button(second_frame,text="Add  to cart",bg="black",fg="white")
        add_to_cart.grid(row=5,column=1,columnspan=4)



def ball_description(product_image,product_price,product_info):
        #============= clear the screen
    for ele in main_frame.winfo_children():
        ele.destroy()

    ball_details_mainframe(product_image,product_price,product_info)




        #----------------------       clothing product        ------------------------------




def details_mainframe(product_image,product_price,product_info):

                #--------------------- funtion to dipaly size

        def size_value(product_size):
                size_display.delete(0,END)
                size_display.insert(0,product_size)

        global main_frame

        main_frame = Frame(root,bg="#ffffff")
        main_frame.place(x=0, y=90)

        my_canvas = Canvas(main_frame, width=1500, height=740,bg="#ffffff")
        my_canvas.pack(side=LEFT, fill=BOTH)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, padx=5, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

        second_frame = Frame(my_canvas, width=1500, height=740,bg="#ffffff")


        my_canvas.create_window((0, 0), window=second_frame)


        passed_image = Label(second_frame, image=product_image, bg="white", borderwidth=0)
        passed_image.grid(row=0,column=0,ipadx=40,ipady=70,rowspan=10)

        passed_image_price=Label(second_frame,text=product_price)
        passed_image_price.grid(row=1,column=1,columnspan=3)

        passed_image_info=Label(second_frame,text=product_info)
        passed_image_info.grid(row=2,column=1,columnspan=3)

        size_label=Label(second_frame,text="Size")
        size_label.grid(row=3,column=1)
        size_display=Entry(second_frame,width=4)
        size_display.grid(row=3,column=2)

        Large=Button(second_frame,text="Large",bg="black",fg="white",command=lambda : size_value("L"))
        Large.grid(row=4,column=1)
        Medium=Button(second_frame,text="Medium",bg="black",fg="white",command=lambda : size_value("M"))
        Medium.grid(row=4,column=2)
        small=Button(second_frame,text="small",bg="black",fg="white",command=lambda : size_value("S"))
        small.grid(row=4,column=3)

        add_to_cart=Button(second_frame,text="Add  to cart",bg="black",fg="white")
        add_to_cart.grid(row=5,column=1,columnspan=3)



        #-----------------------        Clearing the screen passing image --------------------

def description(product_image,product_price,product_info):
        #============= clear the screen
    for ele in main_frame.winfo_children():
        ele.destroy()

    details_mainframe(product_image,product_price,product_info)




        #-----------------------     Cart     --------------------------- 


                #------------------      adding cart function        ----------------- 
def add_to_cart():
        pass




                #-------------------    for your prodcut cart     --------------------------------


def cart_window():

        global main_frame

        main_frame = Frame(root,bg="#ffffff")
        main_frame.place(x=0, y=90)

        my_canvas = Canvas(main_frame, width=1500, height=740,bg="#ffffff")
        my_canvas.pack(side=LEFT, fill=BOTH)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, padx=5, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

        second_frame = Frame(my_canvas, width=1500, height=740,bg="#ffffff")


        my_canvas.create_window((0, 0), window=second_frame)

        add_to_cart=Button(second_frame,text="Add  to cart")
        add_to_cart.grid(row=1,column=1)
        


def cart_frame():
    for ele in main_frame.winfo_children():
        ele.destroy()

    cart_window()
                


        #---------------        product through search          -----------------------------



def search_frame():


        global main_frame

        main_frame = Frame(root,bg="#ffffff")
        main_frame.place(x=0, y=90)

        my_canvas = Canvas(main_frame, width=1500, height=740,bg="#ffffff")
        my_canvas.pack(side=LEFT, fill=BOTH)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, padx=5, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

        second_frame = Frame(my_canvas, width=1500, height=740,bg="#ffffff")


        my_canvas.create_window((0, 880), window=second_frame)


                        #---------------         Football search        -----------------------------
        
        if search_entry.get()=="Football" or search_entry.get()=="football" or search_entry.get()=="soccer":

                search_entry.delete(0,END)

                b1 = Button(second_frame, image=F1, bg="white", borderwidth=0,command=lambda : description(F1,"Rs 1150","Adidas Real Madrid Jersy(White)"))
                b1.grid(row=1,column=0)
                price=Label(second_frame,text="Rs 1150")
                price.grid(row=2,column=0)
                l11=Label(second_frame,text="Adidas Real Madrid Jersy(White)")
                l11.grid(row=3,column=0)


                b2 = Button(second_frame, image=F2, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F2,"Rs 1150","Nike PSG Jersy(Blue)"))
                b2.grid(row=1,column=1)
                price=Label(second_frame,text="Rs 1150")
                price.grid(row=2,column=1)
                l22=Label(second_frame,text="Nike PSG Jersy(Blue)")
                l22.grid(row=3,column=1)


                b3 = Button(second_frame, image=F3, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F3,"Rs 5000","Jordan Messi PSG Jersy(Blue)"))
                b3.grid(row=1,column=2)
                price=Label(second_frame,text="Rs 5000")
                price.grid(row=2,column=2)
                l33=Label(second_frame,text="Jordan Messi PSG Jersy(Blue)")
                l33.grid(row=3,column=2)


                b4 = Button(second_frame, image=F4, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F4,"Rs 3000","Addidas Manchester United Jersy(Red)"))
                b4.grid(row=4,column=3)
                price=Label(second_frame,text="Rs 3000")
                price.grid(row=5,column=3)
                l44=Label(second_frame,text="Addidas Manchester United Jersy(Red)")
                l44.grid(row=6,column=3)


                b5 = Button(second_frame, image=F5, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F5,"Rs 3000","Addidas Modrić Real Madrid Jersy(Pink)"))
                b5.grid(row=4,column=0)
                price=Label(second_frame,text="Rs 3000")
                price.grid(row=5,column=0)
                l55=Label(second_frame,text="Addidas Modrić Real Madrid Jersy(Pink)")
                l55.grid(row=6,column=0)


                b6 = Button(second_frame, image=F6, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F6,"Rs 2500","Addidas Bayern Munich Jersy(Red)"))
                b6.grid(row=4,column=1)
                price=Label(second_frame,text="Rs 2500")
                price.grid(row=5,column=1)
                l44=Label(second_frame,text="Addidas Bayern Munich Jersy(Red)")
                l44.grid(row=6,column=1)

                b7 = Button(second_frame, image=G1, bg="white", borderwidth=0,command=lambda : description(G1,"Rs 1150","Smaple Women jersey(pink)"))
                b7.grid(row=7,column=2)
                price=Label(second_frame,text="Rs 1150")
                price.grid(row=8,column=2)
                l11=Label(second_frame,text="Smaple Women jersey(pink)")
                l11.grid(row=9,column=2)


                b8 = Button(second_frame, image=G2, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(G2,"Rs 1150","Addidas Germany Home Jersey(White)"))
                b8.grid(row=7,column=3)
                price=Label(second_frame,text="Rs 1150")
                price.grid(row=8,column=3)
                l22=Label(second_frame,text="Addidas Germany Home Jersey(White)")
                l22.grid(row=9,column=3)


                b9 = Button(second_frame, image=G3, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(G3,"Rs 5000","Nike Brazil Home Jersey(Yellow)"))
                b9.grid(row=7,column=0)
                price=Label(second_frame,text="Rs 5000")
                price.grid(row=8,column=0)
                l33=Label(second_frame,text="Nike Brazil Home Jersey(Yellow)")
                l33.grid(row=9,column=0)


                b10 = Button(second_frame, image=G4, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(G4,"Rs 5000","Addidas Arsenal Jersey(Red)"))
                b10.grid(row=7,column=1)
                price=Label(second_frame,text="Rs 5000")
                price.grid(row=8,column=1)
                l44=Label(second_frame,text="Addidas Arsenal Jersey(Red)")
                l44.grid(row=9,column=1)


                b11 = Button(second_frame, image=G5, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(G5,"Rs 5000","Addidas Belgium Home Jersey(Red)"))
                b11.grid(row=10,column=2)
                price=Label(second_frame,text="Rs 5000")
                price.grid(row=11,column=2)
                l55=Label(second_frame,text="Addidas Belgium Home Jersey(Red)")
                l55.grid(row=12,column=2)




                b12 = Button(second_frame, image=G6, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(G6,"Rs 5000","Nike Livepool Jersey(Red)"))
                b12.grid(row=10,column=3)
                price=Label(second_frame,text="Rs 5000")
                price.grid(row=11,column=3)
                l55=Label(second_frame,text="Nike Livepool Jersey(Red)")
                l55.grid(row=12,column=3)

                b13 = Button(second_frame, image=G7, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(G7,"Rs 5000","Nike Chelsea Jersey(Blue)"))
                b13.grid(row=10,column=0)
                price=Label(second_frame,text="Rs 5000")
                price.grid(row=11,column=0)
                l55=Label(second_frame,text="Nike Chelsea Jersey(Blue)")
                l55.grid(row=12,column=0)
                
                b14 = Button(second_frame, image=G8, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(G8,"Rs 5000","Addidas Juventus Jersey(white)"))
                b14.grid(row=4,column=2)
                price=Label(second_frame,text="Rs 5000")
                price.grid(row=5,column=2)
                l55=Label(second_frame,text="Addidas Juventus Jersey(white)")
                l55.grid(row=6,column=2)

                b15 = Button(second_frame, image=F7, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F7,"Rs 5000","Adiddas Ronaldo Manchester United Jersy(Red)"))
                b15.grid(row=1,column=3)
                price=Label(second_frame,text="Rs 5000")
                price.grid(row=2,column=3)
                l44=Label(second_frame,text="Adiddas Ronaldo Manchester United Jersy(Red)")
                l44.grid(row=3,column=3)
                

                        #--------------------         basketball search         -----------------------------------


        if search_entry.get()=="basketball" or search_entry.get()=="Basketball":

                b1 = Button(second_frame, image=BB1, bg="white", borderwidth=0,command=lambda : description(BB1,"Rs 1150","Nike LA Lakers Jersy(Yellow)"))
                b1.grid(row=1,column=0)
                price=Label(second_frame,text="Rs 1150")
                price.grid(row=2,column=0)
                l11=Label(second_frame,text="Nike LA Lakers Jersy(Yellow)")
                l11.grid(row=3,column=0)


                b2 = Button(second_frame, image=BB2, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(BB2,"Rs 1150","Jordan Chicago Bulls Jersey(Red)"))
                b2.grid(row=1,column=1)
                price=Label(second_frame,text="Rs 1150")
                price.grid(row=2,column=1)
                l22=Label(second_frame,text="Jordan Chicago Bulls Jersey(Red)")
                l22.grid(row=3,column=1)


                b3 = Button(second_frame, image=BB3, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(BB3,"Rs 5000","Jordan Boston Celetics Jersey(Black)"))
                b3.grid(row=1,column=2)
                price=Label(second_frame,text="Rs 5000")
                price.grid(row=2,column=2)
                l33=Label(second_frame,text="Jordan Boston Celetics Jersey(Black)")
                l33.grid(row=3,column=2)


                b4 = Button(second_frame, image=BB4, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(BB4,"Rs 5000","Nike Raptors Toronto Jesrey(White)"))
                b4.grid(row=4,column=0)
                price=Label(second_frame,text="Rs 5000")
                price.grid(row=5,column=0)
                l44=Label(second_frame,text="Nike Raptors Toronto Jesrey(White)")
                l44.grid(row=6,column=0)


                b5 = Button(second_frame, image=BB5, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(BB5,"Rs 5000","Nike Dallas Jersy(Blue)"))
                b5.grid(row=4,column=1)
                price=Label(second_frame,text="Rs 5000")
                price.grid(row=5,column=1)
                l55=Label(second_frame,text="Nike Dallas Jersy(Blue)")
                l55.grid(row=6,column=1)


                b6 = Button(second_frame,image=BB6, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(BB6,"Rs 500","Nike Villanova Jersey(Blue)"))
                b6.grid(row=4,column=2)
                price=Label(second_frame,text="Rs 5000")
                price.grid(row=5,column=2)
                l55=Label(second_frame,text="Nike Villanova Jersey(Blue)")
                l55.grid(row=6,column=2)

                b7 = Button(second_frame, image=BB7, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(BB7,"Rs 5000","Sample Basketball Jersy(White)"))
                b7.grid(row=1,column=3)
                price=Label(second_frame,text="Rs 5000")
                price.grid(row=2,column=3)
                l55=Label(second_frame,text="Sample Basketball Jersey(White)")
                l55.grid(row=3,column=3)


                #---------------------------            ball search           ---------------------------


        if search_entry.get()=="ball" or search_entry.get()=="Ball" or search_entry.get()=="balls" or search_entry.get()=="Balls" or search_entry.get()=="BALL" or search_entry.get()=="BALLS":

                b1 = Button(second_frame, image=Ball1, bg="white", borderwidth=0,command=lambda : ball_description(Ball1,"Rs 1150","Wilson Ball"))
                b1.grid(row=1,column=0)
                price=Label(second_frame,text="Rs 1150")
                price.grid(row=2,column=0)
                l11=Label(second_frame,text="Wilson Ball")
                l11.grid(row=3,column=0)


                b2 = Button(second_frame, image=Ball2, bg="white", relief=GROOVE,borderwidth=0,command=lambda : ball_description(Ball2,"Rs 1150","NBA Ball"))
                b2.grid(row=1,column=1)
                price=Label(second_frame,text="Rs 1150")
                price.grid(row=2,column=1)
                l22=Label(second_frame,text="NBA Ball")
                l22.grid(row=3,column=1)


                b3 = Button(second_frame, image=Ball3, bg="white", relief=GROOVE,borderwidth=0,command=lambda : ball_description(Ball3,"Rs 5000","Wilson Leather Ball"))
                b3.grid(row=1,column=2)
                price=Label(second_frame,text="Rs 5000")
                price.grid(row=2,column=2)
                l33=Label(second_frame,text="Wilson Leather Ball")
                l33.grid(row=3,column=2)


                b4 = Button(second_frame, image=Ball4, bg="white", relief=GROOVE,borderwidth=0,command=lambda : ball_description(Ball4,"Rs 5000","Nike Elite Ball"))
                b4.grid(row=1,column=3)
                price=Label(second_frame,text="Rs 5000")
                price.grid(row=2,column=3)
                l44=Label(second_frame,text="Nike Elite Ball")
                l44.grid(row=3,column=3)



                b5 = Button(second_frame, image=Ball5, bg="white", borderwidth=0,command=lambda : ball_description(Ball5,"Rs 1150","NIKE PL BALL"))
                b5.grid(row=4,column=0)
                price=Label(second_frame,text="Rs 1150")
                price.grid(row=5,column=0)
                l11=Label(second_frame,text="NIKE PL BALL")
                l11.grid(row=6,column=0)


                b6 = Button(second_frame, image=Ball6, bg="white", relief=GROOVE,borderwidth=0,command=lambda : ball_description(Ball6,"Rs 1150","Addidas Telstar WC 18 Ball"))
                b6.grid(row=4,column=1)
                price=Label(second_frame,text="Rs 1150")
                price.grid(row=5,column=1)
                l22=Label(second_frame,text="Addidas Telstar WC 18 Ball")
                l22.grid(row=6,column=1)


                b7 = Button(second_frame, image=Ball7, bg="white", relief=GROOVE,borderwidth=0,command=lambda : ball_description(Ball7,"Rs 5000","Classic Black & White Ball"))
                b7.grid(row=4,column=2)
                price=Label(second_frame,text="Rs 5000")
                price.grid(row=5,column=2)
                l33=Label(second_frame,text="Classic Black & White Ball")
                l33.grid(row=6,column=2)


                b8 = Button(second_frame, image=Ball8, bg="white", relief=GROOVE,borderwidth=0,command=lambda : ball_description(Ball8,"Rs 5000","UEFA Ball"))
                b8.grid(row=4,column=3)
                price=Label(second_frame,text="Rs 5000")
                price.grid(row=5,column=3)
                l44=Label(second_frame,text="UEFA Ball")
                l44.grid(row=6,column=3)


                b9 = Button(second_frame, image=Ball9, bg="white", relief=GROOVE,borderwidth=0,command=lambda : ball_description(Ball9,"Rs 5000","Addidas Euro 2020 Ball"))
                b9.grid(row=7,column=0)
                price=Label(second_frame,text="Rs 5000")
                price.grid(row=8,column=0)
                l55=Label(second_frame,text="Addidas Euro 2020 Ball")
                l55.grid(row=9,column=0)


                b10 = Button(second_frame, image=Ball10, bg="white", relief=GROOVE,borderwidth=0,command=lambda : ball_description(Ball10,"Rs 5000","Addidas Brazuca WC 14 Ball"))
                b10.grid(row=7,column=1)
                price=Label(second_frame,text="Rs 5000")
                price.grid(row=8,column=1)
                l44=Label(second_frame,text="Addidas Brazuca WC 14 Ball")
                l44.grid(row=9,column=1)

                b11 = Button(second_frame, image=Ball11, bg="white", borderwidth=0,command=lambda : ball_description(Ball11,"Rs 1150","Alex Ball"))
                b11.grid(row=1,column=4)
                price=Label(second_frame,text="Rs 1150")
                price.grid(row=2,column=4)
                l11=Label(second_frame,text="Alex Ball")
                l11.grid(row=3,column=4)

                b12 = Button(second_frame, image=Ball12, bg="white", borderwidth=0,command=lambda : ball_description(Ball12,"Rs 1150","Puma Ball"))
                b12.grid(row=4,column=4)
                price=Label(second_frame,text="Rs 1150")
                price.grid(row=5,column=4)
                l11=Label(second_frame,text="Puma Ball")
                l11.grid(row=6,column=4)
        

                #--------------------------------    else result        ------------------


        else:
                error_label=Label(second_frame,text="Opps! Cant't find the item (TRY AGAIN)")
                error_label.pack(side=TOP)



def search_window():

        if search_entry.get()=="":
        
                pass
        else:
                for ele in main_frame.winfo_children():
                        ele.destroy()

                search_frame()




        #---------------------------   Ball Frame       --------------------------------



def ball_frame():

        global main_frame

        main_frame = Frame(root,bg="#ffffff")
        main_frame.place(x=0, y=90)

        my_canvas = Canvas(main_frame, width=1500, height=740,bg="#ffffff")
        my_canvas.pack(side=LEFT, fill=BOTH)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, padx=5, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

        second_frame = Frame(my_canvas, width=1500, height=740,bg="#ffffff")


        my_canvas.create_window((0, 800), window=second_frame)

        b1 = Button(second_frame, image=Ball1, bg="white", borderwidth=0,command=lambda : ball_description(Ball1,"Rs 1150","Wilson Ball"))
        b1.grid(row=1,column=0)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=2,column=0)
        l11=Label(second_frame,text="Wilson Ball")
        l11.grid(row=3,column=0)


        b2 = Button(second_frame, image=Ball2, bg="white", relief=GROOVE,borderwidth=0,command=lambda : ball_description(Ball2,"Rs 1150","NBA Ball"))
        b2.grid(row=1,column=1)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=2,column=1)
        l22=Label(second_frame,text="NBA Ball")
        l22.grid(row=3,column=1)


        b3 = Button(second_frame, image=Ball3, bg="white", relief=GROOVE,borderwidth=0,command=lambda : ball_description(Ball3,"Rs 5000","Wilson Leather Ball"))
        b3.grid(row=1,column=2)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=2,column=2)
        l33=Label(second_frame,text="Wilson Leather Ball")
        l33.grid(row=3,column=2)


        b4 = Button(second_frame, image=Ball4, bg="white", relief=GROOVE,borderwidth=0,command=lambda : ball_description(Ball4,"Rs 5000","Nike Elite Ball"))
        b4.grid(row=1,column=3)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=2,column=3)
        l44=Label(second_frame,text="Nike Elite Ball")
        l44.grid(row=3,column=3)



        b5 = Button(second_frame, image=Ball5, bg="white", borderwidth=0,command=lambda : ball_description(Ball5,"Rs 1150","NIKE PL BALL"))
        b5.grid(row=4,column=0)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=5,column=0)
        l11=Label(second_frame,text="NIKE PL BALL")
        l11.grid(row=6,column=0)


        b6 = Button(second_frame, image=Ball6, bg="white", relief=GROOVE,borderwidth=0,command=lambda : ball_description(Ball6,"Rs 1150","Addidas Telstar WC 18 Ball"))
        b6.grid(row=4,column=1)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=5,column=1)
        l22=Label(second_frame,text="Addidas Telstar WC 18 Ball")
        l22.grid(row=6,column=1)


        b7 = Button(second_frame, image=Ball7, bg="white", relief=GROOVE,borderwidth=0,command=lambda : ball_description(Ball7,"Rs 5000","Classic Black & White Ball"))
        b7.grid(row=4,column=2)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=5,column=2)
        l33=Label(second_frame,text="Classic Black & White Ball")
        l33.grid(row=6,column=2)


        b8 = Button(second_frame, image=Ball8, bg="white", relief=GROOVE,borderwidth=0,command=lambda : ball_description(Ball8,"Rs 5000","UEFA Ball"))
        b8.grid(row=4,column=3)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=5,column=3)
        l44=Label(second_frame,text="UEFA Ball")
        l44.grid(row=6,column=3)


        b9 = Button(second_frame, image=Ball9, bg="white", relief=GROOVE,borderwidth=0,command=lambda : ball_description(Ball9,"Rs 5000","Addidas Euro 2020 Ball"))
        b9.grid(row=7,column=0)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=8,column=0)
        l55=Label(second_frame,text="Addidas Euro 2020 Ball")
        l55.grid(row=9,column=0)


        b10 = Button(second_frame, image=Ball10, bg="white", relief=GROOVE,borderwidth=0,command=lambda : ball_description(Ball10,"Rs 5000","Addidas Brazuca WC 14 Ball"))
        b10.grid(row=7,column=1)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=8,column=1)
        l44=Label(second_frame,text="Addidas Brazuca WC 14 Ball")
        l44.grid(row=9,column=1)

        b11 = Button(second_frame, image=Ball11, bg="white", borderwidth=0,command=lambda : ball_description(Ball11,"Rs 1150","Alex Ball"))
        b11.grid(row=1,column=4)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=2,column=4)
        l11=Label(second_frame,text="Alex Ball")
        l11.grid(row=3,column=4)

        b12 = Button(second_frame, image=Ball12, bg="white", borderwidth=0,command=lambda : ball_description(Ball12,"Rs 1150","Puma Ball"))
        b12.grid(row=4,column=4)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=5,column=4)
        l11=Label(second_frame,text="Puma Ball")
        l11.grid(row=6,column=4)


def ball_window():

    for ele in main_frame.winfo_children():
        ele.destroy()

    ball_frame()



        #-------------------------   men football wear frame    --------------------

        

def men_football_frame():

        global main_frame


                #----------------    Creating a Frame  --------------------------

        main_frame = Frame(root,bg="#ffffff")
        main_frame.place(x=0, y=90)

        my_canvas = Canvas(main_frame, width=1500, height=740,bg="#ffffff")
        my_canvas.pack(side=LEFT, fill=BOTH)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, padx=5, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

        second_frame = Frame(my_canvas, width=1500, height=740,bg="#ffffff")


        my_canvas.create_window((0,880), window=second_frame)



        b1 = Button(second_frame, image=F1, bg="white", borderwidth=0,command=lambda : description(F1,"Rs 1150","Adidas Real Madrid Jersy(White)"))
        b1.grid(row=1,column=0)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=2,column=0)
        l11=Label(second_frame,text="Adidas Real Madrid Jersy(White)")
        l11.grid(row=3,column=0)


        b2 = Button(second_frame, image=F2, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F2,"Rs 1150","Nike PSG Jersy(Blue)"))
        b2.grid(row=1,column=1)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=2,column=1)
        l22=Label(second_frame,text="Nike PSG Jersy(Blue)")
        l22.grid(row=3,column=1)


        b3 = Button(second_frame, image=F3, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F3,"Rs 5000","Jordan Messi PSG Jersy(Blue)"))
        b3.grid(row=1,column=2)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=2,column=2)
        l33=Label(second_frame,text="Jordan Messi PSG Jersy(Blue)")
        l33.grid(row=3,column=2)


        b4 = Button(second_frame, image=F4, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F4,"Rs 3000","Addidas Manchester United Jersy(Red)"))
        b4.grid(row=4,column=0)
        price=Label(second_frame,text="Rs 3000")
        price.grid(row=5,column=0)
        l44=Label(second_frame,text="Addidas Manchester United Jersy(Red)")
        l44.grid(row=6,column=0)


        b5 = Button(second_frame, image=F5, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F5,"Rs 3000","Addidas Modrić Real Madrid Jersy(Pink)"))
        b5.grid(row=4,column=1)
        price=Label(second_frame,text="Rs 3000")
        price.grid(row=5,column=1)
        l55=Label(second_frame,text="Addidas Modrić Real Madrid Jersy(Pink)")
        l55.grid(row=6,column=1)


        b6 = Button(second_frame, image=F6, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F6,"Rs 2500","Addidas Bayern Munich Jersy(Red)"))
        b6.grid(row=4,column=2)
        price=Label(second_frame,text="Rs 2500")
        price.grid(row=5,column=2)
        l44=Label(second_frame,text="Addidas Bayern Munich Jersy(Red)")
        l44.grid(row=6,column=2)

        b7 = Button(second_frame, image=F8, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F8,"Rs 2500","Addidas Bayern Munich Jersy(Red)"))
        b7.grid(row=1,column=4)
        price=Label(second_frame,text="Rs 2500")
        price.grid(row=2,column=4)
        l44=Label(second_frame,text="Nike Liverpool Jersey (Red)")
        l44.grid(row=3,column=4)
        
        b9 = Button(second_frame, image=F7, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F7,"Rs 5000","Adiddas Ronaldo Manchester United Jersy(Red)"))
        b9.grid(row=4,column=4)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=5,column=4)
        l44=Label(second_frame,text="Adiddas Ronaldo Manchester United Jersy(Red)")
        l44.grid(row=6,column=4)


def m_football_window():

        for ele in main_frame.winfo_children():
            ele.destroy()

        men_football_frame()



        #----------     football women wear frame       -------------------------------------------


def female_football_frame():
        
        global main_frame


                #----------------    Creating a Frame  --------------------------

        main_frame = Frame(root,bg="#ffffff")
        main_frame.place(x=0, y=90)

        my_canvas = Canvas(main_frame, width=1500, height=740,bg="#ffffff")
        my_canvas.pack(side=LEFT, fill=BOTH)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, padx=5, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

        second_frame = Frame(my_canvas, width=1500, height=740,bg="#ffffff")

        my_canvas.create_window((0,880), window=second_frame)



        b1 = Button(second_frame, image=G1, bg="white", borderwidth=0,command=lambda : description(G1,"Rs 1150","Smaple Women jersey(pink)"))
        b1.grid(row=1,column=0)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=2,column=0)
        l11=Label(second_frame,text="Smaple Women jersey(pink)")
        l11.grid(row=3,column=0)


        b2 = Button(second_frame, image=G2, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(G2,"Rs 1150","Addidas Germany Home Jersey(White)"))
        b2.grid(row=1,column=1)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=2,column=1)
        l22=Label(second_frame,text="Addidas Germany Home Jersey(White)")
        l22.grid(row=3,column=1)


        b3 = Button(second_frame, image=G3, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(G3,"Rs 5000","Nike Brazil Home Jersey(Yellow)"))
        b3.grid(row=4,column=0)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=5,column=0)
        l33=Label(second_frame,text="Nike Brazil Home Jersey(Yellow)")
        l33.grid(row=6,column=0)


        b4 = Button(second_frame, image=G4, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(G4,"Rs 5000","Addidas Arsenal Jersey(Red)"))
        b4.grid(row=4,column=1)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=5,column=1)
        l44=Label(second_frame,text="Addidas Arsenal Jersey(Red)")
        l44.grid(row=6,column=1)


        b5 = Button(second_frame, image=G5, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(G5,"Rs 5000","Addidas Belgium Home Jersey(Red)"))
        b5.grid(row=4,column=3)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=5,column=3)
        l55=Label(second_frame,text="Addidas Belgium Home Jersey(Red)")
        l55.grid(row=6,column=3)




        b6 = Button(second_frame, image=G6, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(G6,"Rs 5000","Addidas Belgium Home Jersey(Red)"))
        b6.grid(row=4,column=2)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=5,column=2)
        l55=Label(second_frame,text="Addidas Belgium Home Jersey(Red)")
        l55.grid(row=6,column=2)

        b7 = Button(second_frame, image=G7, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(G7,"Rs 5000","Addidas Belgium Home Jersey(Red)"))
        b7.grid(row=1,column=2)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=2,column=2)
        l55=Label(second_frame,text="Addidas Belgium Home Jersey(Red)")
        l55.grid(row=3,column=2)
        
        b8 = Button(second_frame, image=G8, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(G8,"Rs 5000","Addidas Belgium Home Jersey(Red)"))
        b8.grid(row=1,column=3)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=2,column=3)
        l55=Label(second_frame,text="Addidas Belgium Home Jersey(Red)")
        l55.grid(row=3,column=3)


def f_football_window():

        for ele in main_frame.winfo_children():
            ele.destroy()

        female_football_frame()




def Basketball_frame():
        
        global main_frame


                #----------------    Creating a Frame  --------------------------

        main_frame = Frame(root,bg="#ffffff")
        main_frame.place(x=0, y=90)

        my_canvas = Canvas(main_frame, width=1500, height=740,bg="#ffffff")
        my_canvas.pack(side=LEFT, fill=BOTH)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, padx=5, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

        second_frame = Frame(my_canvas, width=1500, height=740,bg="#ffffff")


        my_canvas.create_window((0,880), window=second_frame)

        
        b1 = Button(second_frame, image=BB1, bg="white", borderwidth=0,command=lambda : description(BB1,"Rs 1150","Nike LA Lakers Jersy(Yellow)"))
        b1.grid(row=1,column=0)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=2,column=0)
        l11=Label(second_frame,text="Nike LA Lakers Jersy(Yellow)")
        l11.grid(row=3,column=0)


        b2 = Button(second_frame, image=BB2, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(BB2,"Rs 1150","Jordan Chicago Bulls Jersey(Red)"))
        b2.grid(row=1,column=1)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=2,column=1)
        l22=Label(second_frame,text="Jordan Chicago Bulls Jersey(Red)")
        l22.grid(row=3,column=1)


        b3 = Button(second_frame, image=BB3, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(BB3,"Rs 5000","Jordan Boston Celetics Jersey(Black)"))
        b3.grid(row=1,column=2)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=2,column=2)
        l33=Label(second_frame,text="Jordan Boston Celetics Jersey(Black)")
        l33.grid(row=3,column=2)


        b4 = Button(second_frame, image=BB4, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(BB4,"Rs 5000","Nike Raptors Toronto Jesrey(White)"))
        b4.grid(row=4,column=0)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=5,column=0)
        l44=Label(second_frame,text="Nike Raptors Toronto Jesrey(White)")
        l44.grid(row=6,column=0)


        b5 = Button(second_frame, image=BB5, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(BB5,"Rs 5000","Nike Dallas Jersy(Blue)"))
        b5.grid(row=4,column=1)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=5,column=1)
        l55=Label(second_frame,text="Nike Dallas Jersy(Blue)")
        l55.grid(row=6,column=1)


        b6 = Button(second_frame,image=BB6, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(BB6,"Rs 500","Nike Villanova Jersey(Blue)"))
        b6.grid(row=4,column=2)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=5,column=2)
        l55=Label(second_frame,text="Nike Villanova Jersey(Blue)")
        l55.grid(row=6,column=2)

        b7 = Button(second_frame, image=BB7, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(BB7,"Rs 5000","Sample Basketball Jersy(White)"))
        b7.grid(row=1,column=3)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=2,column=3)
        l55=Label(second_frame,text="Sample Basketball Jersey(White)")
        l55.grid(row=3,column=3)


def mf_Basketball_window():

        for ele in main_frame.winfo_children():
            ele.destroy()

        Basketball_frame()
















#=====================================        Database        ================================================================

conn=sqlite3.connect('register.db')

c=conn.cursor()




        #--------------------        Table for database       -------------------

# c.execute(""" CREATE TABLE login(
        
#         name String NOT NULL,
#         username String PRIMARY KEY,
#         email String NOT NULL,
#         phoneno Integer NOT NULL,
#         password String NOT NULL

#         )""")

      


        #-----------------------      passing username through argyument     --------------------

parser = ArgumentParser()
parser.add_argument("-u", "--user")

args = vars(parser.parse_args())
user = args['user']





#============================================       GUI        =============================================================



#-----------------------        Images     ---------------------------------------------


logo=Image.open("Home\sw.png")
search=Image.open("Home\search.png")
profile=Image.open("Home\profile.png")
contact=Image.open("Home\contact.png")
cart=Image.open("Home\cart.png")

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





        #---------------------         offer image     --------------------


offer=Image.open("Dress\offer.png")
offer1=Image.open("Dress\offer1.png")
offer2=Image.open("Dress\offer2.jpg")

offer=offer.resize((1500,500),Image.ANTIALIAS)
offer1=offer1.resize((1500,500),Image.ANTIALIAS)
offer2=offer2.resize((1500,500),Image.ANTIALIAS)

offer_img=ImageTk.PhotoImage(offer)
offer1_img=ImageTk.PhotoImage(offer1)
offer2_img=ImageTk.PhotoImage(offer2)

offer_list=[offer_img,offer1_img,offer2_img]




        #----------------------------------      Shopping Product     -----------------

F1 = Image.open("Dress\F1.jpg")
F2 = Image.open("Dress\F2.jpg")
F3 = Image.open("Dress\F3.png")
F4 = Image.open("Dress\F4.jpg")
F5 = Image.open("Dress\F5.jpg")
F6 = Image.open("Dress\F6.jpg")
F7 = Image.open("Dress\F7.png")
F8 = Image.open("Dress\F8.jpg")

B1 = Image.open("Dress\B1.jpg")
B2 = Image.open("Dress\B2.jpg")


F1 = F1.resize((380, 380), Image.ANTIALIAS)
F2 = F2.resize((380, 380), Image.ANTIALIAS)
F3 = F3.resize((380, 380), Image.ANTIALIAS)
F4 = F4.resize((380, 380), Image.ANTIALIAS)
F5 = F5.resize((380, 380), Image.ANTIALIAS)
F6 = F6.resize((380, 380), Image.ANTIALIAS)
F7 = F7.resize((380, 380), Image.ANTIALIAS)
F8 = F8.resize((380, 380), Image.ANTIALIAS)


B1 = B1.resize((380, 380), Image.ANTIALIAS)
B2 = B2.resize((380, 380), Image.ANTIALIAS)

F1 = ImageTk.PhotoImage(F1)
F2 = ImageTk.PhotoImage(F2)
F3 = ImageTk.PhotoImage(F3)
F4 = ImageTk.PhotoImage(F4)
F5 = ImageTk.PhotoImage(F5)
F6 = ImageTk.PhotoImage(F6)
F7 = ImageTk.PhotoImage(F7)
F8 = ImageTk.PhotoImage(F8)


B1 = ImageTk.PhotoImage(B1)
B2= ImageTk.PhotoImage(B2)


        #------------------------------         ball images     ----------

Ball1 = Image.open("Balls1\B1.jpg")
Ball2 = Image.open("Balls1\B2.png")
Ball3 = Image.open("Balls1\B3.jpg")
Ball4 = Image.open("Balls1\B4.jpg")
Ball5 = Image.open("Balls\B1.jpg")
Ball6 = Image.open("Balls\B2.jpg")
Ball7 = Image.open("Balls\B3.jpg")
Ball8 = Image.open("Balls\B4.jpg")
Ball9 = Image.open("Balls\B5.jpg")
Ball10 = Image.open("Balls\B6.jpg")
Ball11 = Image.open("Balls1\B5.jpg")
Ball12 = Image.open("Balls\B7.jpg")





Ball1 = Ball1.resize((300, 300), Image.ANTIALIAS)
Ball2 = Ball2.resize((300, 300), Image.ANTIALIAS)
Ball3 = Ball3.resize((300, 300), Image.ANTIALIAS)
Ball4 = Ball4.resize((300, 300), Image.ANTIALIAS)
Ball5 = Ball5.resize((300, 300), Image.ANTIALIAS)
Ball6= Ball6.resize((300, 300), Image.ANTIALIAS)
Ball7 = Ball7.resize((300, 300), Image.ANTIALIAS)
Ball8 = Ball8.resize((300, 300), Image.ANTIALIAS)
Ball9 = Ball9.resize((300, 300), Image.ANTIALIAS)
Ball10 = Ball10.resize((300, 300), Image.ANTIALIAS)
Ball11 = Ball11.resize((300, 300), Image.ANTIALIAS)
Ball12 = Ball12.resize((300, 300), Image.ANTIALIAS)




Ball1 = ImageTk.PhotoImage(Ball1)
Ball2 = ImageTk.PhotoImage(Ball2)
Ball3 = ImageTk.PhotoImage(Ball3)
Ball4 = ImageTk.PhotoImage(Ball4)
Ball5 = ImageTk.PhotoImage(Ball5)
Ball6 = ImageTk.PhotoImage(Ball6)
Ball7 = ImageTk.PhotoImage(Ball7)
Ball8 = ImageTk.PhotoImage(Ball8)
Ball9 = ImageTk.PhotoImage(Ball9)
Ball10 = ImageTk.PhotoImage(Ball10)
Ball11 = ImageTk.PhotoImage(Ball11)
Ball12 = ImageTk.PhotoImage(Ball12)




        #-----------------      female dress   -------------------------------

G1 = Image.open("Girl\F1.jpg")
G2 = Image.open("Girl\F2.jpg")
G3 = Image.open("Girl\F3.jpg")
G4 = Image.open("Girl\F4.jpg")
G5 = Image.open("Girl\F5.jpg")
G6 = Image.open("Girl\F6.jpg")
G7 = Image.open("Girl\F7.jpg")
G8 = Image.open("Girl\F8.jpg")






G1 = G1.resize((370, 370), Image.ANTIALIAS)
G2 = G2.resize((370, 370), Image.ANTIALIAS)
G3 = G3.resize((370, 370), Image.ANTIALIAS)
G4 = G4.resize((370, 370), Image.ANTIALIAS)
G5 = G5.resize((370, 370), Image.ANTIALIAS)
G6 = G6.resize((370, 370), Image.ANTIALIAS)
G7 = G7.resize((370, 370), Image.ANTIALIAS)
G8 = G8.resize((370, 370), Image.ANTIALIAS)



G1 = ImageTk.PhotoImage(G1)
G2 = ImageTk.PhotoImage(G2)
G3 = ImageTk.PhotoImage(G3)
G4 = ImageTk.PhotoImage(G4)
G5 = ImageTk.PhotoImage(G5)
G6 = ImageTk.PhotoImage(G6)
G7 = ImageTk.PhotoImage(G7)
G8 = ImageTk.PhotoImage(G8)




          #-------------------Basketball dresses-----------------------------------------------------------#


BB1 = Image.open("Dress\B1.jpg")
BB2 = Image.open("Dress\B2.jpg")
BB3 = Image.open("Dress\B3.jpg")
BB4 = Image.open("Dress\B4.jpg")
BB5 = Image.open("Dress\B5.jpg")
BB6 = Image.open("Dress\B6.jpg")
BB7 = Image.open("Dress\B7.jpg")





BB1 = BB1.resize((380, 380), Image.ANTIALIAS)
BB2 = BB2.resize((380, 380), Image.ANTIALIAS)
BB3 = BB3.resize((380, 380), Image.ANTIALIAS)
BB4 = BB4.resize((380, 380), Image.ANTIALIAS)
BB5 = BB5.resize((380, 380), Image.ANTIALIAS)
BB6 = BB6.resize((380, 380), Image.ANTIALIAS)
BB7 = BB7.resize((380, 380), Image.ANTIALIAS)





BB1 = ImageTk.PhotoImage(BB1)
BB2= ImageTk.PhotoImage(BB2)
BB3 = ImageTk.PhotoImage(BB3)
BB4= ImageTk.PhotoImage(BB4)
BB5 = ImageTk.PhotoImage(BB5)
BB6 = ImageTk.PhotoImage(BB6)
BB7 = ImageTk.PhotoImage(BB7)











        #------------------------   Headlines    ------------------------------

logo_button=Button(root,image=logo_img,borderwidth=0,command=back_home)
logo_button.place(x=0,y=0)

search_entry=Entry(root,width=75,fg="black",justify="right",borderwidth=2,font="50")
search_entry.place(x=320,y=0,height=50)

search_button=Button(root,image=search_img,borderwidth=0,command=search_window)
search_button.place(x=1160,y=0)

cart_button=Button(root,image=cart_img,borderwidth=0,command=cart_frame)
cart_button.place(x=1250,y=0)

contact_button=Button(root,image=contact_img,borderwidth=0)
contact_button.place(x=1310,y=0)






        #---------------------    Label for Username   --------------------------------


welcome_label=Label(root,text="WELCOME!")
welcome_label.place(x=1420,y=0)

try:
        c.execute('SELECT * FROM login WHERE username = ?',(user,))

        records=c.fetchone()
        username=records[1]



        username_label=Label(root,text=username)
        username_label.place(x=1420,y=15)

except:
        pass


        #-------------------     Profile pic     ------------------------

profile_button=Button(root,image=profile_img,borderwidth=0,command=run_login)
profile_button.place(x=1500,y=0)





        #---------------------------------     Menu  BUttons     --------------------------


mb1 = Menubutton(root, text="MENS       ▼", relief=GROOVE, padx=25, pady=8, bg="black", fg="white")
mb1.place(x=320, y=50)
mb1.menu = Menu(mb1, tearoff=0, bg="white", fg="black")
mb1["menu"] = mb1.menu
mb2 = Menu(mb1, tearoff=0, bg="white", fg="black")
mb2.add_command(label="Wear", activebackground="black", activeforeground="white",command=m_football_window)
mb2.add_separator()
mb2.add_command(label="Balls", activebackground="black", activeforeground="white")

mb0 = Menu(mb1, tearoff=0, bg="white", fg="black")
mb0.add_command(label="Wear", activebackground="black", activeforeground="white",command=mf_Basketball_window)
mb0.add_separator()
mb0.add_command(label="Balls", activebackground="black", activeforeground="white")



mb1.menu.add_cascade(label="Football", menu=mb2, activebackground="black", activeforeground="white")
mb1.menu.add_separator()
mb1.menu.add_cascade(label="Basketball", menu=mb0, activebackground="black", activeforeground="white")



mb3 = Menubutton(root, text="WOMENS       ▼", relief=GROOVE, padx=25, pady=8, bg="black", fg="white")
mb3.place(x=650, y=50)
mb3.menu = Menu(mb3, tearoff=0, bg="white", fg="black")
mb3["menu"] = mb3.menu
mb4 = Menu(mb3, tearoff=0, bg="white", fg="black")
mb4.add_command(label="Wear", activebackground="black", activeforeground="white",command=f_football_window)
mb4.add_separator()
mb4.add_command(label="Balls", activebackground="black", activeforeground="white")


mb7 = Menu(mb3, tearoff=0, bg="white", fg="black")
mb7.add_command(label="Wear", activebackground="black", activeforeground="white",command=mf_Basketball_window)
mb7.add_separator()
mb7.add_command(label="Balls", activebackground="black", activeforeground="white")


mb3.menu.add_cascade(label="Football", menu=mb4, activebackground="black", activeforeground="white")
mb3.menu.add_separator()
mb3.menu.add_cascade(label="Basketball", menu=mb7, activebackground="black", activeforeground="white")

mb5 = Button(root, text="⚽    Balls    ⚽", relief=GROOVE, padx=25, pady=4, bg="black", fg="white",command=ball_window)
mb5.place(x=955, y=50)

mb6 = Button(root, text="⌂ HOME", relief=GROOVE, padx=25, pady=4, bg="black", fg="white",command=back_home )
mb6.place(x=2, y=52)

        



      
        #-------------------    Function for Home Page       ---------------------------------


            

                #--------------------------     mainframe       --------------------------

def mainframe():

        global main_frame


                #----------------    Creating a Frame  --------------------------

        main_frame = Frame(root,bg="#ffffff")
        main_frame.place(x=0, y=90)

        my_canvas = Canvas(main_frame, width=1500, height=740,bg="#ffffff")
        my_canvas.pack(side=LEFT, fill=BOTH)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, padx=5, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

        second_frame = Frame(my_canvas, width=1500, height=740,bg="#ffffff")


        my_canvas.create_window((0,880), window=second_frame)




                #------------------------   All product Labeling  --------------------------------


        offer_random=random.randint(0,2)
        offer_label=Label(second_frame,image=offer_list[offer_random])
        offer_label.grid(row=0,column=0,columnspan=3)


        b1 = Button(second_frame, image=F1, bg="white", borderwidth=0,command=lambda : description(F1,"Rs 1150","Adidas Real Madrid Jersy(White)"))
        b1.grid(row=1,column=0)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=2,column=0)
        l11=Label(second_frame,text="Adidas Real Madrid Jersy(White)")
        l11.grid(row=3,column=0)


        b2 = Button(second_frame, image=F2, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F2,"Rs 1150","Nike PSG Jersy(Blue)"))
        b2.grid(row=1,column=1)
        price=Label(second_frame,text="Rs 1150")
        price.grid(row=2,column=1)
        l22=Label(second_frame,text="Nike PSG Jersy(Blue)")
        l22.grid(row=3,column=1)


        b3 = Button(second_frame, image=F3, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F3,"Rs 5000","Jordan Messi PSG Jersy(Blue)"))
        b3.grid(row=1,column=2)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=2,column=2)
        l33=Label(second_frame,text="Jordan Messi PSG Jersy(Blue)")
        l33.grid(row=3,column=2)


        b4 = Button(second_frame, image=F4, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F4,"Rs 3000","Addidas Manchester United Jersy(Red)"))
        b4.grid(row=4,column=0)
        price=Label(second_frame,text="Rs 3000")
        price.grid(row=5,column=0)
        l44=Label(second_frame,text="Addidas Manchester United Jersy(Red)")
        l44.grid(row=6,column=0)


        b5 = Button(second_frame, image=F5, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F5,"Rs 3000","Addidas Modrić Real Madrid Jersy(Pink)"))
        b5.grid(row=4,column=1)
        price=Label(second_frame,text="Rs 3000")
        price.grid(row=5,column=1)
        l55=Label(second_frame,text="Addidas Modrić Real Madrid Jersy(Pink)")
        l55.grid(row=6,column=1)


        b6 = Button(second_frame, image=F6, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F6,"Rs 2500","Addidas Bayern Munich Jersy(Red)"))
        b6.grid(row=4,column=2)
        price=Label(second_frame,text="Rs 2500")
        price.grid(row=5,column=2)
        l44=Label(second_frame,text="Addidas Bayern Munich Jersy(Red)")
        l44.grid(row=6,column=2)


        b7 = Button(second_frame, image=B1, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(B1,"Rs 4000","Nike LA Lakers Jersy(Yellow)"))
        b7.grid(row=7,column=0)
        price=Label(second_frame,text="Rs 4000")
        price.grid(row=8,column=0)
        l44=Label(second_frame,text="Nike LA Lakers Jersy(Yellow)")
        l44.grid(row=9,column=0)


        b8 = Button(second_frame, image=B2, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(B2,"Rs 5000","Jordan Chicago Bull Jersy(Red)"))
        b8.grid(row=7,column=1)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=8,column=1)
        l44=Label(second_frame,text="Jordan Chicago Bull Jersy(Red)")
        l44.grid(row=9,column=1)




        b9 = Button(second_frame, image=F7, bg="white", relief=GROOVE,borderwidth=0,command=lambda : description(F7,"Rs 5000","Adiddas Ronaldo Manchester United Jersy(Red)"))
        b9.grid(row=7,column=2)
        price=Label(second_frame,text="Rs 5000")
        price.grid(row=8,column=2)
        l44=Label(second_frame,text="Adiddas Ronaldo Manchester United Jersy(Red)")
        l44.grid(row=9,column=2)






mainframe()



conn.commit()
conn.close()




root.mainloop()