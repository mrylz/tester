print("1 - para cekme")
print("2 - para yatırma")
print("3 - bakiye sorgulama")
print("4 - menü")
bakiye = int(input("bakiye : "))
islem = int(input("hangi işlemi yapmak istersiniz : "))
if(islem==4):
    def menu(isim):
        isim = str(input("isim : "))
        return f"Hoşgeldiniz {isim}"
    print(menu("isim"))
elif(islem==1):
    def paracekme(miktar):
        miktar = int(input("Tutar : "))
        return "kalan bakiyeniz : " + str(bakiye - miktar)
    print(paracekme("miktar"))
elif(islem==2):
    def parayatirma(tips):
        tips = int(input("Tutar : "))
        return "yeni bakiyeniz : " + str(bakiye + tips)
    print(parayatirma("tips"))
elif(islem == 3):
    def bakiyeSorgu():
        return bakiye
    print(bakiyeSorgu())
else:
    print("lütfen başka bi seçenek seçiniz")

