import mysql.connector

def connect_db():
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678',
        database='ipek_pismaniye'
    )
    return con

def pismaniye_ekle(isim, fiyat, adet ):
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
    print(urunler)
    return urunler


def pismaniye_guncelle(urun_id, yeni_isim=None, yeni_fiyat=None, yeni_adet=None):
    con = connect_db()
    cursor = con.cursor()
    yeni_isim = input("Yeni ürün adı: ")
    yeni_fiyat = int(input("Yeni ürün fiyatı: "))
    yeni_adet = int(input("Yeni adet: "))
    if yeni_isim:
        cursor.execute("UPDATE pismaniyeler SET isim = %s WHERE id = %s", (yeni_isim, urun_id))
    if yeni_fiyat:
        cursor.execute("UPDATE pismaniyeler SET fiyat = %s WHERE id = %s", (yeni_fiyat, urun_id))
    if yeni_adet:
        cursor.execute("UPDATE pismaniyeler SET fiyat = %s WHERE id = %s", (yeni_adet, urun_id))
    con.commit()
    con.close()

def pismaniye_sil(urun_id):
    con = connect_db()
    cursor = con.cursor()
    cursor.execute("DELETE FROM pismaniyeler WHERE id = %s", (urun_id,))
    con.commit()
    con.close()

def kestane_sekeri_ekle(isim, fiyat, adet):
    con = connect_db()
    cursor = con.cursor()
    cursor.execute("""
    INSERT INTO kestane_sekerleri (isim, fiyat, adet) VALUES (%s, %s, %s)
    """, (isim, fiyat, adet))
    con.commit()
    con.close()

def kestane_sekeri_listele():
    con = connect_db()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM kestane_sekerleri")
    urunler = cursor.fetchall()
    con.close()
    print(urunler)
    return urunler

def kestane_sekeri_guncelle(urun_id, yeni_isim=None, yeni_fiyat=None, yeni_adet=None):
    con = connect_db()
    cursor = con.cursor()
    yeni_isim = input("Yeni ürün adı: ")
    yeni_fiyat = int(input("Yeni ürün fiyatı: "))
    yeni_adet = int(input("Yeni adet: "))
    if yeni_isim:
        cursor.execute("UPDATE kestane_sekerleri SET isim = %s WHERE id = %s", (yeni_isim, urun_id))
    if yeni_fiyat:
        cursor.execute("UPDATE kestane_sekerleri SET fiyat = %s WHERE id = %s", (yeni_fiyat, urun_id))
    if yeni_adet:
        cursor.execute("UPDATE pismaniyeler SET fiyat = %s WHERE id = %s", (yeni_adet, urun_id))   
    con.commit()
    con.close()

def kestane_sekeri_sil(urun_id):
    con = connect_db()
    cursor = con.cursor()
    cursor.execute("DELETE FROM kestane_sekerleri WHERE id = %s", (urun_id,))
    con.commit()
    con.close()

def cekme_helvalar_ekle(isim, fiyat, adet):
    con = connect_db()
    cursor = con.cursor()
    cursor.execute("""
    INSERT INTO cekme_helvalar (isim, fiyat, adet) VALUES (%s, %s, %s)
    """, (isim, fiyat, adet))
    con.commit()
    con.close()

def cekme_helvalar_listele():
    con = connect_db()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM cekme_helvalar")
    urunler = cursor.fetchall()
    con.close()
    print(urunler)
    return urunler

def cekme_helvalar_guncelle(urun_id, yeni_isim=None, yeni_fiyat=None, yeni_adet=None):
    con = connect_db()
    cursor = con.cursor()
    yeni_isim = input("Yeni ürün adı: ")
    yeni_fiyat = int(input("Yeni ürün fiyatı: "))
    yeni_adet = int(input("Yeni adet: "))
    if yeni_isim:
        cursor.execute("UPDATE cekme_helvalar SET isim = %s WHERE id = %s", (yeni_isim, urun_id))
    if yeni_fiyat:
        cursor.execute("UPDATE cekme_helvalar SET fiyat = %s WHERE id = %s", (yeni_fiyat, urun_id))
    if yeni_adet:
        cursor.execute("UPDATE pismaniyeler SET fiyat = %s WHERE id = %s", (yeni_adet, urun_id))
    con.commit()
    con.close()

def cekme_helvalar_sil(urun_id):
    con = connect_db()
    cursor = con.cursor()
    cursor.execute("DELETE FROM cekme_helvalar WHERE id = %s", (urun_id,))
    con.commit()
    con.close()

class Muhasebe:
    def __init__(self):
        self.fiyat_list = []
        self.urun_id = []

    def sayim(self):
        con = connect_db()
        cursor = con.cursor()
        pismaniye_isim = []
        cekme_helva_isim = []
        kestane_sekeri_isim = []
        cekme_helva_data = []
        kestane_sekeri_data = []
        pismaniye_data = []
        
        cursor.execute("SELECT * FROM pismaniyeler")
        pismaniye_data = cursor.fetchall()
        cursor.execute("SELECT * FROM kestane_sekerleri")
        kestane_sekeri_data = cursor.fetchall()
        cursor.execute("SELECT * FROM cekme_helvalar")
        cekme_helva_data = cursor.fetchall()
        
        cursor.execute("SELECT isim FROM pismaniyeler")
        pismaniye_isim = [row[0] for row in cursor.fetchall()]
        cursor.execute("SELECT isim FROM kestane_sekerleri")
        kestane_sekeri_isim = [row[0] for row in cursor.fetchall()]
        cursor.execute("SELECT isim FROM cekme_helvalar")
        cekme_helva_isim = [row[0] for row in cursor.fetchall()]
        
        cursor.close()
        con.close()
        
        return pismaniye_data, kestane_sekeri_data, cekme_helva_data, pismaniye_isim, kestane_sekeri_isim, cekme_helva_isim

    def yeni_stok(self, pismaniye_data, kestane_sekeri_data, cekme_helva_data, pismaniye_isim, kestane_sekeri_isim, cekme_helva_isim):
        con = connect_db()
        cursor = con.cursor()
        
        for isim in pismaniye_isim:
            yeni_adet = int(input(f"{isim} yeni adet: "))
            cursor.execute("UPDATE pismaniyeler SET adet = %s WHERE isim = %s", (yeni_adet, isim))
        
        for isim in kestane_sekeri_isim:
            yeni_adet = int(input(f"{isim} yeni adet: "))
            cursor.execute("UPDATE kestane_sekerleri SET adet = %s WHERE isim = %s", (yeni_adet, isim))
        
        for isim in cekme_helva_isim:
            yeni_adet = int(input(f"{isim} yeni adet: "))
            cursor.execute("UPDATE cekme_helvalar SET adet = %s WHERE isim = %s", (yeni_adet, isim))
        
        con.commit()
        cursor.close()
        con.close()
