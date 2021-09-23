import sqlite3
from PIL import Image,ImageTk


        #------------------     database for image          -------------------------------

image_database=sqlite3.connect("image.db")
image_cursor=image_database.cursor()

# image_cursor.execute("""

#         CREATE TABLE IF NOT EXIST image_table (image_name TEXT,image_date BLOB)

# """)


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

#------------------women basketball products-----------------------


FB1 = Image.open("Bgirl\B1.jpg")
FB2 = Image.open("Bgirl\B2.jpg")
FB3 = Image.open("Bgirl\B3.jpg")
FB4 = Image.open("Bgirl\B4.jpg")
FB5 = Image.open("Bgirl\B5.jpg")
FB6 = Image.open("Bgirl\B6.jpg")






FB1 = FB1.resize((380, 380), Image.ANTIALIAS)
FB2 = FB2.resize((380, 380), Image.ANTIALIAS)
FB3 = FB3.resize((380, 380), Image.ANTIALIAS)
FB4 = FB4.resize((380, 380), Image.ANTIALIAS)
FB5 = FB5.resize((380, 380), Image.ANTIALIAS)
FB6 = FB6.resize((380, 380), Image.ANTIALIAS)







FB1 = ImageTk.PhotoImage(FB1)
FB2= ImageTk.PhotoImage(FB2)
FB3 = ImageTk.PhotoImage(FB3)
FB4= ImageTk.PhotoImage(FB4)
FB5 = ImageTk.PhotoImage(FB5)
FB6 = ImageTk.PhotoImage(FB6)






image_cursor.execute("""

        INSERT INTO image_table(image_name,image_data) VALUES (?,?)

""",
        ("F1",F1)
        ("F2",F2)
        ("F3",F3)
        ("F4",F4)
        ("F5",F5)
        ("F6",F6)
        ("F7",F7)
        ("F8",F8)

)



image_database.commit()

image_database.close()