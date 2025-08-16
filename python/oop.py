class product:
    def __init__(self,name,price,isActive):
        self.name = name
        self.price = price
        self.isActive = isActive

        
p1 = product("İphone 15",60000,False)
p2 = product("İphone 15 Pro",70000,True)
p3 = product("İphone 15 Max",80000,True)
urunler = [p1,p2,p3]
for urun in urunler:
    if urun.isActive==True:
        print(f"Ürün adı : {urun.name} Ürün fiyatı : {urun.price} Stok Durumu : Stokta")
    else:
        print(f"Ürün adı : {urun.name} Ürün fiyatı : {urun.price} Stok Durumu : Stokta Yok")
