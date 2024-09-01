from model import pismaniye_ekle,pismaniye_guncelle,pismaniye_sil,pismaniyeleri_listele,kestane_sekeri_ekle,kestane_sekeri_guncelle,kestane_sekeri_listele,kestane_sekeri_sil,cekme_helvalar_ekle,cekme_helvalar_guncelle,cekme_helvalar_listele,cekme_helvalar_sil

def urun_ekleme():
    print("""
------------------------------------------------
                İPEK PİŞMANİYE          
    1 ) Pişmaniye
    2 ) Kestane Şekeri
    3 ) Çekme Helva
    4 ) çıkış
------------------------------------------------""")
    
    eklenicek_urun_turu = int(input("Ürün Türünü Seçiniz: "))
    isim = input("İsim: ")
    fiyat = int(input("Fiyat: "))
    adet = int(input("Adet: "))
    kod = int(input("Kod: "))
    while True:
        if eklenicek_urun_turu ==1:
            pismaniye_ekle(isim,fiyat,adet,kod)
            print(f"{isim, fiyat, adet, kod} Ürün başarı ile eklenmiştir.")
            break
        elif eklenicek_urun_turu ==2:
            kestane_sekeri_ekle(isim,fiyat,adet,kod)
            print(f"{isim, fiyat, adet, kod} Ürün başarı ile eklenmiştir.")
            break
        elif eklenicek_urun_turu ==3:
            cekme_helvalar_ekle(isim,fiyat,adet,kod)
            print(f"{isim, fiyat, adet, kod} Ürün başarı ile eklenmiştir.")
            break
        elif eklenicek_urun_turu==4:
            break
        else:
            raise ValueError

def urun_guncelleme(self,yeni_isim,yeni_fiyat,yeni_adet,yeni_kod):
    print("""
------------------------------------------------
                İPEK PİŞMANİYE          
    1 ) Pişmaniye
    2 ) Kestane Şekeri
    3 ) Çekme Helva
    4 ) çıkış
------------------------------------------------""")
    self.yeni_isim = input("Yeni isim: ")
    self.yeni_fiyat = int(input("Yeni fiyat: "))
    self.yeni_adet = int(input("Yeni adet: "))
    self.yeni_kod = int(input("Yeni kod: "))
    while True:
        guncelleme_secim = int(input("Güncellemek istediğiniz ürün kategorisi: "))
        if guncelleme_secim ==1:
            pismaniye_guncelle(yeni_isim,yeni_fiyat,yeni_adet,yeni_kod)
            break
        elif guncelleme_secim ==2:
            kestane_sekeri_guncelle(yeni_isim,yeni_fiyat,yeni_adet,yeni_kod)
            break
        elif guncelleme_secim ==3:
            cekme_helvalar_guncelle(yeni_isim,yeni_fiyat,yeni_adet,yeni_kod)
            break
        elif guncelleme_secim ==4:
            break
        else: 
            raise ValueError
        
def urun_silme():
    print("""
------------------------------------------------
                İPEK PİŞMANİYE          
    1 ) Pişmaniye
    2 ) Kestane Şekeri
    3 ) Çekme Helva
    4 ) çıkış
------------------------------------------------""")
    
    silme_secim = int(input("Silmek istediğiniz ürün kategorisi: "))
    if silme_secim ==1:
        pismaniyeleri_listele()
        silinecek_urun_id = int(input("Silmek istediğiniz ürünün id'si: "))
        pismaniye_sil(silinecek_urun_id)
    elif silme_secim ==2:
        kestane_sekeri_listele()
        silinecek_urun_id = int(input("Silmek istediğiniz ürünün id'si: "))
        kestane_sekeri_sil(silinecek_urun_id)
    elif silme_secim ==3:
        cekme_helvalar_listele()
        silinecek_urun_id = int(input("Silmek istediğiniz ürünün id'si: "))
        cekme_helvalar_sil(silinecek_urun_id)
    elif silme_secim ==4:
        print("Çıkış yaptınız!")
    else: 
        raise ValueError
        
