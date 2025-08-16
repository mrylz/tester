markalar = ["opel","bmw","audi"]
for marka in enumerate(markalar,1):
    print(marka)
    #enumerate metodu ile index numaralarını yazabilir ona göre işlem yapabiliriz o yüzden kolaylık sağlar
#1 sayısı başlangıç değerinin gösteriri default değer 0 dır
numara = [100,200,300]
ogrenci = ["ali","hasan","ayse"]
print(list(zip(numara,ogrenci)))
for no,isim in zip(numara,ogrenci):
    print(no,isim)

    #zip ilede iki listeyi birleştirme işlemini daha kolay yapabiliriz
    