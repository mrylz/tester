"""

    Dosya açmak ve oluşturmak için open() fonksiyonu  kullanılır.
    Kullanımı  : open(dosya_adi,dosya_erişme_modu)
    dosya_erişme_modu : dosyayı hangi amaçla açtığımızı belirtir.
    "r" okuma  modu : okuma modu.belirtilen konumda dosya olamlıdır.
    seek : cursor konumu

    "w" : (Write) yazma modu.
    ** Dosyayı konumda  oluşturur.
    ** Eğer konumda  aynı dosya varsa dosyayı siler ve yeni oluşturur.

    "a" : (Append) ekleme. Dosya konumda yoksa oluşturulur.
    "r+" : Hem okuma hem yazma modunda açılır. Dosya  konumda yoksa hata verir.
    
"""
