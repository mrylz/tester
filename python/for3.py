urunler = [
    {"urunAdi":"HP Victus" , "Fiyat" : 32999},
    {"urunAdi":"LENOVO Thinkpad" , "Fiyat" : 25999},
    {"urunAdi":"APPLE Macbook" , "Fiyat" : 49999},
    {"urunAdi":"HUAWEİ Matebook" , "Fiyat" : 26999},
    {"urunAdi":"CASPER Nirvana" , "Fiyat" : 20000}

]
kelime = str(input("lütfen anahtar keimeyi giriniz : "))
toplam = 0
for x in urunler:
    print(f"{x['urunAdi']} marka ürünün fiyatı {x['Fiyat']} Türk Lirası")
    toplam = toplam + x['Fiyat']

    if(x['Fiyat']>= 25000 and x['Fiyat']<=40000):
        print(f"{x['urunAdi']} marka ürünün fiyatı {x['Fiyat']} Türk Lirası")
    if(kelime == x['urunAdi']):
        print(f"{x['urunAdi']} marka ürünün fiyatı {x['Fiyat']} Türk Lirası")
print("ürünlerintoplam  fiyatı : " + str(toplam))