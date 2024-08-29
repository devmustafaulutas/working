import mysql.connector

def connect_db():
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678',
        database='ipek_pismaniye'
    )
    return con

con = connect_db()
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS kestane_sekerleri(
    id INT AUTO_INCREMENT PRIMARY KEY,
    isim VARCHAR(100),
    fiyat INT,
    adet INT,
    kod INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS cekme_helvalar(
    id INT AUTO_INCREMENT PRIMARY KEY,
    isim VARCHAR(100),
    fiyat INT,
    adet INT,
    kod INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pismaniyeler (
    id INT AUTO_INCREMENT PRIMARY KEY,
    isim VARCHAR(100),
    fiyat INT,
    adet INT,
    kod INT
)
""")

con.close()
