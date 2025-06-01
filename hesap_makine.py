sayi1 = int(input("1.Sayı : "))
sayi2 = int(input("2.Sayı : "))
print("Toplam : " + str(sayi1 + sayi2))
if sayi1 > sayi2:
    print("Fark : " + str(sayi1 - sayi2))
else:
    print("Fark : " + str(sayi2 - sayi1))
if sayi1 > sayi2:
    print("Bölüm : " + str(sayi1 / sayi2))
else:
    print("Bölüm : " + str(sayi2 / sayi1))
print("Çarpım : " + str(sayi1 * sayi2))