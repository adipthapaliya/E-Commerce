from tkinter import *
from PIL import Image,ImageTk
import sqlite3


root=Tk()


image_database=sqlite3.connect("image.db")
image_cursor=image_database.cursor()

# image_cursor.execute("""

#         CREATE TABLE IF NOT EXIST image_table (image_name TEXT,image_date BLOB)

# """)


image_cursor.execute("""
    SELECT * FROM image_table

""")


image_database.commit()

image_database.close()

root.mainloop()