import mysql.connector

def connect_db():
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678',
        database='ipek_pismaniye'
    )
    return con

class Querys:
    def __init__(self):
        self.con = connect_db()
        self.cursor = self.con.cursor()

    def close_connection(self):
        self.cursor.close()
        self.con.close()

    def all_products(self):
        all_products = []
        query = """
        SELECT id, name, quantity, price FROM pismaniyeler
        UNION
        SELECT id, name, quantity, price FROM kestane_sekerleri
        UNION
        SELECT id, name, quantity, price FROM cekme_helvalar;
        """
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        all_products.extend(data)
        print(all_products)
    
    def products(self,category):
        products  = []
        self.cursor.execute(f"SELECT * FROM {category}")
        data = self.cursor.fetchall()
        products.extend(data)
        print(products)

    def add_product(self,category,name,quantity,price):
        query = f"INSERT INTO {category} (name,quantity,price) VALUES (%s,%s,%s)"
        values = (name,quantity,price)
        try:
            self.cursor.execute(query, values)
            self.con.commit()
            print("Product added successfully!")

        except mysql.connector.Error as error:
            print("Failed to add product: {}".format(error))
            self.con.rollback()

        finally:
            self.close_connection()

    def del_product(self,category,id):
        query = f"DELETE FROM {category} WHERE id = {id}"
        try:
            self.cursor.execute(query)
            self.con.commit()
            print("Product deleted successfully!")

        except mysql.connector.Error as error:
            print("Failed to delete product: {}".format(error))
            self.con.rollback()
        finally:
            self.close_connection()


    def update_product(self, category, product_id, new_name, new_piece, new_price):
        
        query = f"UPDATE {category} SET name = %s, quantity = %s, price = %s WHERE id = %s"
        values = (new_name, new_piece, new_price, product_id)

        try:
            self.cursor.execute(query, values)
            self.con.commit()
            print("Product updated successfully!")

        except mysql.connector.Error as error:
            print("Failed to update product: {}".format(error))
            self.con.rollback()

        finally:
            self.close_connection()


# query = Querys()
# query.all_tables()


class Tables:

    def __init__(self):
        self.con = connect_db()
        self.cursor = self.con.cursor()
    
    def all_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS pismaniyeler (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            quantity INT,
            price INT,
            code INT
        )""")

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS kestane_sekerleri (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            quantity INT,
            price INT,
            code INT
        )
        """)       
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS cekme_helvalar (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            quantity INT,
            price INT,
            code INT
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS restock (
            id INT AUTO_INCREMENT PRIMARY KEY,
            date DATE NOT NULL,
            restock_bill INT,
            category VARCHAR(100),
            code INT,
            quantity INT
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily_reports (
            id INT AUTO_INCREMENT PRIMARY KEY,
            date DATE NOT NULL,
            daily_sales INT NOT NULL,
            cash INT NOT NULL,
            credit_card INT,
            expenses  INT,
            discounts  INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
        """)
        self.cursor.close()
        self.con.close()