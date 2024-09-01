import mysql.connector

def connect_db():
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678',
        database='ipek_pismaniye'
    )
    return con

def pismaniye_ekle(isim, fiyat, adet):
    con = connect_db()
    cursor = con.cursor()
    cursor.execute("""
    INSERT INTO pismaniyeler (isim, fiyat, adet) VALUES (%s, %s, %s)
    """, (isim, fiyat, adet))
    con.commit()
    con.close()

def pismaniyeleri_listele():
    con = connect_db()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM pismaniyeler")
    urunler = cursor.fetchall()
    con.close()
    return urunler

def pismaniye_guncelle(urun_id, yeni_isim=None, yeni_fiyat=None):
    con = connect_db()
    cursor = con.cursor()
    if yeni_isim:
        cursor.execute("UPDATE pismaniyeler SET isim = %s WHERE id = %s", (yeni_isim, urun_id))
    if yeni_fiyat:
        cursor.execute("UPDATE pismaniyeler SET fiyat = %s WHERE id = %s", (yeni_fiyat, urun_id))
    con.commit()
    con.close()

def pismaniye_sil(urun_id):
    con = connect_db()
    cursor = con.cursor()
    cursor.execute("DELETE FROM pismaniyeler WHERE id = %s", (urun_id,))
    con.commit()
    con.close()

# Tablo oluşturma işlemi
con = connect_db()
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pismaniyeler (
    id INT AUTO_INCREMENT PRIMARY KEY,
    isim VARCHAR(100),
    fiyat INT,
    adet INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS saray_helvaları(
    id INT AUTO_INCREMENT PRIMARY KEY,
    isim VARCHAR(100),
    fiyat INT,
    adet INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS kestane_sekerleri(
    id INT AUTO_INCREMENT PRIMARY KEY,
    isim VARCHAR(100),
    fiyat INT,
    adet INT
)
""")

con.close()
