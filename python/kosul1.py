km = int(input("kilometre : "))
yakit = str(input("yakıt : "))
if(yakit == "benzin"):
    sonuc = 39.35 * km
    print("toplam tutar : " + str(sonuc))
elif(yakit == "dizel"):
    sonuc = 41.71 * km
    print("toplam tutar : " + str(sonuc))
elif(yakit == "lpg"):
   sonuc = 20.28 * km
   print("toplam tutar : " + str(sonuc))
else:
    print("geçersiz yakıt türü girdiniz")


    