from model import pismaniye_ekle,pismaniye_guncelle,pismaniye_sil,pismaniyeleri_listele,kestane_sekeri_ekle,kestane_sekeri_guncelle,kestane_sekeri_listele,kestane_sekeri_sil,cekme_helvalar_ekle,cekme_helvalar_guncelle,cekme_helvalar_listele,cekme_helvalar_sil
from arayuz import urun_kategori,anamenu,urunler,muhasebe
from functions import urun_ekleme,urun_silme,muhasebe_func

while True:
    anamenu()
    secim = int(input("Seçiminiz: "))
    if secim == 1:
        urunler()
        urunler_secim = int(input("Seçiminiz: "))
        if urunler_secim == 1:
            urun_kategori()
            a = int(input('Seçiminiz: '))
            if a == 1:
                pismaniyeleri_listele()
            elif a==2:
                cekme_helvalar_listele()
            elif a==3:
                kestane_sekeri_listele()
            elif secim ==4:
                break
            else:
                raise ValueError
        elif urunler_secim == 2:
            urun_kategori()
            a = int(input('Seçiminiz: '))
            if a == 1:
                pismaniyeleri_listele()
                urun_id = int(input("Güncellemek istediğiniz ürün idsi: "))
                pismaniye_guncelle(urun_id)
            elif a==2:
                cekme_helvalar_listele()
                urun_id = int(input("Güncellemek istediğiniz ürün idsi: "))
                cekme_helvalar_guncelle(urun_id)
            elif a==3:
                kestane_sekeri_listele()
                urun_id = int(input("Güncellemek istediğiniz ürün idsi: "))
                kestane_sekeri_guncelle(urun_id)
            elif secim ==4:
                break
            else:
                raise ValueError
        elif urunler_secim == 3:
            urun_silme()
        elif urunler_secim ==4:
            urun_ekleme()
        elif urunler_secim == 5:
            break
        else:
            raise ValueError
    elif secim ==2:
        muhasebe()
        urunler_secim2 = int(input("Seçiminiz: "))
        if urunler_secim2 ==1:
            muhasebe_func()
        elif urunler_secim2 ==2:
            break
        else:
            raise ValueError
    elif secim ==3:
        break
    else:
        raise ValueError

