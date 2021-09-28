
from tkinter import *
import sqlite3

root=Tk()
root.title("Product details")
root.geometry('400x580')
root.resizable(FALSE, FALSE)
root.iconbitmap("Home/logo.ico")

#===================================         function to show customer details       ===========================================


def show_details():
    conn=sqlite3.connect('register.db')

    c=conn.cursor()


    # c.execute(""" CREATE TABLE login(
            
    #         name String NOT NULL,
    #         username String PRIMARY KEY,
    #         adress String NOT NULL,
    #         phoneno Integer NOT NULL,
    #         password String NOT NULL,


    #         )""")

    user_name=show_username_entry.get()
    c.execute("SELECT * FROM login WHERE username=?",(user_name,))
    customer_details=c.fetchall()

    for customer in customer_details:
        newwin=Toplevel(root)
        newwin.title("Details")
        newwin.iconbitmap("Home/logo.ico")
        

        username_label=Label(newwin,text="Username")
        username_label.grid(row=0,column=0)

        show_username=Label(newwin,text=customer[1])
        show_username.grid(row=0,column=1)

        adress_label=Label(newwin,text="Adress")
        adress_label.grid(row=1,column=0)

        show_adress=Label(newwin,text=customer[2])
        show_adress.grid(row=1,column=1)

        phoneno_label=Label(newwin,text="Phone no")
        phoneno_label.grid(row=2,column=0)

        show_phoneno=Label(newwin,text=customer[3])
        show_phoneno.grid(row=2,column=1)



    conn.commit()
    conn.close()



#========================================     database for product to delivered       ========================================

product_database=sqlite3.connect("product.db")
product_cursor=product_database.cursor()

# product_cursor.execute("""

#         CREATE TABLE product_table (username TEXT,product_information TEXT,product_cost TEXT)

# """)


#---------------------------------      GUI for order   -----------------------------------------
number=Label(root,text="S/N")
number.grid(row=1,column=0)

username=Label(root,text="Username")
username.grid(row=1,column=1)

product=Label(root,text="Product")
product.grid(row=1,column=2)

price=Label(root,text="Price")
price.grid(row=1,column=3)

product_cursor.execute("SELECT *,oid FROM product_table")

records=product_cursor.fetchall()



i=2
for record in records:
    id_labels=Label(root,text=record[3])
    id_labels.grid(row=i,column=0)

    name=Label(root,text=record[0])
    name.grid(row=i,column=1)

    product_id=Label(root,text=record[1])
    product_id.grid(row=i,column=2)

    product_money=Label(root,text=record[2])
    product_money.grid(row=i,column=3)



    i+=1

#--------------------------------------     frame for search bar of username       ------------------------------------

search_frame=Frame(root)
search_frame.grid(row=0,column=0,columnspan=4,pady=10)

username_label=Label(search_frame,text="Username")
username_label.grid(row=0,column=0)



show_username_entry=Entry(search_frame)
show_username_entry.grid(row=0,column=1,padx=30,pady=10)

details_button=Button(search_frame,text="Show Details",command=show_details)
details_button.grid(row=1,column=0,columnspan=2)





product_database.commit()
product_database.close()



root.mainloop()