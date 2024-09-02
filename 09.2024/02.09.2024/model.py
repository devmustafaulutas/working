import mysql.connector

def connect_db():
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678',
        database='ipek_pismaniye'
    )
    return con

class Tables:

    def __init__(self):
        self.con = connect_db()
        self.cursor = self.con.cursor()
    
    def all_products(self):
        
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS kestane_sekerleri(
            id INT AUTO_INCREMENT PRIMARY KEY,
            isim VARCHAR(100),
            fiyat INT,
            adet INT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS cekme_helvalar(
            id INT AUTO_INCREMENT PRIMARY KEY,
            isim VARCHAR(100),
            fiyat INT,
            adet INT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS pismaniyeler (
            id INT AUTO_INCREMENT PRIMARY KEY,
            isim VARCHAR(100),
            fiyat INT,
            adet INT
        )
        """)
        self.con.close()

class Querys:
    def __init__(self):
        self.con = connect_db()
        self.cursor = self.con.cursor()

    
    def all_products(self):
        self.cursor.execute("""
        SELECT id,isim,adet,fiyat FROM pismaniyeler
        UNION
        SELECT id,isim,adet,fiyat FROM kestane_sekerleri
        UNION
        SELECT id,isim,adet,fiyat FROM cekme_helvalar;
        """)        
        
    def add_product(self,category,name,piece,price):
        query = f"INSERT INTO {category} (isim,adet,fiyat) VALUES (%s,%s,%s)"
        values = (name,piece,price)
        try:
            self.cursor.execute(query, values)
            self.con.commit()
            print("Product added successfully!")

        except mysql.connector.Error as error:
            print("Failed to add product: {}".format(error))
            self.con.rollback()

        finally:
            self.cursor.close()
            self.con.close()

    def del_product(self,category,id):
        self.all_products()
        query = f"DELETE FROM {category} WHERE (id) VALUES (%s)"
        values = (id)
        try:
            self.cursor.execute(query, values)
            self.con.commit()
            print("Product added successfully!")

        except mysql.connector.Error as error:
            print("Failed to add product: {}".format(error))
            self.con.rollback()

        finally:
            self.cursor.close()
            self.con.close()

# query = querys()
# query.all_products()
