not1 = int(input("not1 : ")) 
not2 = int(input("not2 : "))
sözlü = int(input("sözlü : "))
toplam = (not1 + not2 + sözlü) / 3
if((toplam>=0) and (toplam <= 24)):
    print("öğrencinin notu : 0")
elif((toplam>25) and (toplam <= 44)):
    print("öğrencinin notu : 1")
elif((toplam>=45) and (toplam <= 54)):
    print("öğrencinin notu : 2")
elif((toplam>=55) and (toplam <= 69)):
    print("öğrencinin notu : 3")
elif((toplam>=70) and (toplam <= 84)):
    print("öğrencinin notu : 4")
else:
    print("öğrencinin  notu : 5")    






