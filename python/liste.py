araba = ["toyota","bmw","renault","mercedes"]
print(len(araba))
print(araba[0])
print(araba[-1])
araba[2]= "togg"
print(araba)
sonuc = "togg" in araba 
print(sonuc)
print(araba[0:2])
ek =["ford","citroen"]
araba = araba + ek
print(araba)
del araba[-1]
print(araba)
