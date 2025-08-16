try:
    x = int(input("x : "))
    y = int(input("y : "))
    print(x+y)
except:
    print("Hata Oluştu")    
# Farklı hata türlerine farklı işlemler uygulanmalıdır.
try:
    a = int(input("a : "))
    b = int(input("b : "))
    print(a/b)
except ZeroDivisionError:
    print("B ifadesi 0 olamaz")
except ValueError:
    print("B  ifadesiir sayı olmalıdır")
    #Hata ayıklama işlemleri yapılırken 
    """
    import pdb -> bu  modulü dahil ediyoruz
    daha sonra  istediğimiz kısma kadar olan yere ->pdb.set_trace()
    komutlar:
    l -> listeleme
    n -> bir sonraki satıra geçer
    c -> devam etme işlemiyapar
    p -> yazdorma  işlmei yapar
    
    def toplama(a,b,c):
        import pdb;pdb.set_trace()
        return a+b+c
    toplama(10,20,30)    
        
    """
            