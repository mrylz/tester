# # # # # # # benim yaptığı uygulama
# # # # # # # isim = str(input("isim : "))
# # # # # # # def girdi(isim):
# # # # # # #     return "isim = " + isim
# # # # # # # sayi1 = int(input("tekrar sayısı : "))
# # # # # # # def tekrar(sayi1):
# # # # # # #     while(sayi1>0):
# # # # # # #         print(girdi(isim))
# # # # # # #         sayi1 -= 1
# # # # # # # print(tekrar(sayi1))            
# # # # # # hocanın yaptığı
# # # # # # def yazdir(text, adet):
# # # # # #     return text * adet
# # # # # # print(yazdir("merhaba ", 5)
# # # # # #       )
# # # # # benim yaptığım
# # # # # def hesaplaalan(uzunluk,genislik):
# # # # #     return uzunluk *genislik
# # # # # def hesaplacevre(uzunluk,genislik):
# # # # #     return (2*uzunluk) + (2*genislik)
# # # # # print(hesaplaalan(5,7))
# # # # # print(hesaplacevre(8,4))
# # # # hocanın yaptığı
# # # # def hesapla(kisa,uzun):
# # # #     alan = kisa*uzun
# # # #     cevre = 2*(kisa +  uzun)
# # # #     return f"alan : {alan} cevre : {cevre}"
# # # # print(hesapla(4,5))
# # # def yaziTura():
# # #     import random
# # #     sayi = random.random()
# # #     if sayi > 0.5:
# # #         return "Tura"
# # #     else:
# # #         return "Yazı"
# # # print(yaziTura()) 
# # # hocanın yaptığı   
# # def asalSayilar(sayi1,sayi2):
# #     for sayi in range(sayi1,sayi2+1):
# #         if(sayi > 1):
# #             for i in range(2,sayi):
# #                 if(sayi%i==0):
# #                     break
# #             else:
# #                 print(sayi)
# # asalSayilar(10,125) 
# # # benim yaptığım                   
# def bolenBul(sayi1):
#     sayi1 = int(input("sayi : "))
#     for sayi in range(1,sayi1+1):
#         if(sayi1%sayi==0):
#             print(sayi)
# bolenBul("sayi1")




