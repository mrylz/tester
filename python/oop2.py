class BankaHesap:
    def __init__(self,name,bakiye):
        self.name=name
        self.bakiye=0
    def parayatir(self,miktar):
        miktar = int(input("Tutar : "))
        self.bakiye = self.bakiye + miktar
        print(self.bakiye)
    def paracek(self,tutar):
        tutar = int(input("Tutar : "))
        self.bakiye = self.bakiye - tutar
        print(self.bakiye)   
hesap = ("SADIK TURAN")
print(hesap.parayatir())


