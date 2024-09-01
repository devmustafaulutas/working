import json
print("""
-----------Hesap Makinesi-----------
    Hoşgeldiniz!
    İşlem örneği : 15 + 20 (Enter)
    Devam etmek için herhangi bir tuşa basın.
------------------------------------""")
a = input(": ")
print(len(a))
while a!=0:
    break
def hesapmakinesi():
    islem = input(": ")
    islemindeksuzunlugu = (len(islem)) -1
    for i in range(0,1,islemindeksuzunlugu):
        if islem[i]=='+' or islem[i]==''
