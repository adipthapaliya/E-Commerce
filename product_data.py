import sqlite3


        #------------------     database for product          -------------------------------

product_database=sqlite3.connect("product.db")
product_cursor=product_database.cursor()

# product_cursor.execute("""

#         CREATE TABLE product_table (username TEXT,product_information TEXT,product_cost TEXT)

#   """)

product_database.commit()
product_database.close()


