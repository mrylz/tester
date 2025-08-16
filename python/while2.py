n = True
ogrenciler = []
print("ekleme işlemi için + butonuna basınız işlemi bitirmek için - tuşuna basınız")
while(n):
    ogrenciNo = int(input("Öğrenci No : "))
    ogrenciAdi = str(input("Öğrenci Adı : "))
    ogrenciSoyad = str(input("Öğrenci Soyadı : "))
    ogrenciler.append({
        "Öğrenci numarası" : ogrenciNo,
        "Öğrenci adı" : ogrenciAdi,
        "Öğrenci Soyadı" : ogrenciSoyad
    })
    n = bool(input("eklemek için + tuşuna basınız : "))
for x in ogrenciler:
    print(x)
