secim = int(input("Seçim : "))
x = 1
liste = [] 
while x <= secim:
    sayi = int(input("Sayı : "))
    liste.append(sayi)
    x += 1
toplam  = 0    
for x  in liste:
    toplam += x

print("Girdiğiniz  sayıların  ortalaması : " + str(toplam/secim))
