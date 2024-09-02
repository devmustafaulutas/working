import mysql.connector

def connect_db():
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678',
        database='ipek_pismaniye'
    )
    return con

class query:

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
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS hesap(
            id INT AUTO_INCREMENT PRIMARY KEY,
            tarih VARCHAR(10),           
            zrapor INT,
            nakit INT, 
            gider INT,
            kaar INT 
        )""")
        self.con.close()
