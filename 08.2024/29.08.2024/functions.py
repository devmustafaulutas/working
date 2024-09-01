from model import pismaniye_ekle,pismaniye_sil,pismaniyeleri_listele,kestane_sekeri_ekle,kestane_sekeri_listele,kestane_sekeri_sil,cekme_helvalar_ekle,cekme_helvalar_listele,cekme_helvalar_sil

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
    while True:
        if eklenicek_urun_turu ==1:
            pismaniye_ekle(isim,fiyat,adet)
            print(f"{isim, fiyat, adet} Ürün başarı ile eklenmiştir.")
            break
        elif eklenicek_urun_turu ==2:
            kestane_sekeri_ekle(isim,fiyat,adet)
            print(f"{isim, fiyat, adet} Ürün başarı ile eklenmiştir.")
            break
        elif eklenicek_urun_turu ==3:
            cekme_helvalar_ekle(isim,fiyat,adet)
            print(f"{isim, fiyat, adet} Ürün başarı ile eklenmiştir.")
            break
        elif eklenicek_urun_turu==4:
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
    

def muhasebe_func():
    satis = int(input("Günlük pişmaniye satış tutarını giriniz: "))
    kart = int(input("Kart satış miktarını giriniz: "))
    indirim = int(input("Var ise indirim miktarını giriniz: "))
    nakit_pismaniye = int(input("Pişmaniye satışının nakit miktarını giriniz: "))
    gider = int(input("Günlük gider miktarını giriniz: "))

    market = (kart+nakit_pismaniye+gider-indirim)-satis
    toplam_para = kart+nakit_pismaniye+gider
    print(f"{satis} Tl pişmaniye satışınız, {toplam_para} Tl pişmaniyeden kazanılan para, {market} TL marketten kazanılan paradır. Hayırlı işler dileriz")