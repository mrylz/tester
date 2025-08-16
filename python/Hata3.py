def faktoriyel():
    while True:
        x=1
        sonuc = 1
        try:
            sayi = int(input("Sayı : "))
            while x<=sayi:
                sonuc *= x
                x+=1
        except:
            print("lütfen geçerli değerler giriniz ")
        return  sonuc
    
print(faktoriyel())