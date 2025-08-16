

def not_gir():
    ad = str(input("isim : "))
    soyad = str(input("soyad : "))
    not1 = int(input("Not : "))
    not2 = int(input("Not : "))
    not3 = int(input("Not : ")) 
    with open("not.txt","a",encoding="utf-8") as file:
        file.write(ad + '' + soyad + ':' + str(not1) +','+ str(not2) +','+ str(not3) +"\n")
def not_oku():
    with open("not.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))
def not_kaydet():
    with open("not.txt","r",encoding="utf-8") as file:
        liste = []
        for satir in file:
            liste.append(not_hesapla(satir))
        with open("sonucar.txt","w",encoding="utf-8") as  file2:
            file2.writelines(liste)
def not_hesapla():
    satir = satir[:-1]
    liste = satir.split(":")

    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")
    
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = {(not1 + not2 + not3) / 3 }
    if ortalama >= 90 and ortalama <= 100:
        harf = "AA"
    elif ortalama >= 80 and ortalama <=89:
        harf  = "AB"    
    elif ortalama >= 70 and ortalama <=79:
        harf  = "BB"    
    elif ortalama >= 59 and ortalama <=69:
        harf  = "BC"    
    elif ortalama >= 49 and ortalama <=58:
        harf  = "CC"    
    elif ortalama >= 39 and ortalama <=48:
        harf  = "CD"    
    elif ortalama >= 29 and ortalama <38:
        harf  = "DD"    
    elif ortalama >= 19 and ortalama <=28:
        harf  = "DF"
    else:
        harf = "FF"        
    return f"{ogrenciAdi} ':' {harf} ({ortalama})"           
while True:
    secim = int(input("1-Not Gir\n2-Not Oku\n3-Not Kaydet\n4-Çıkış : "))
    if secim == 1:
        not_gir()
    elif secim == 2:
        not_oku()    
    elif secim == 3:
        not_kaydet()
    else:
        break        



