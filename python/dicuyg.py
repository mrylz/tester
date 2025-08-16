ogrenciler_isim = {
101 : 'yiğit bilgi',
102 : 'ada bilgi',
103 : 'çınar turan'
}
ogrenciler_yas = {
101 : 2010,
102 : 2012,
103 : 2017
}
ogrenciler_not = {
101 : (40+80+90),
102 : (80+80+80),
103 : (70+70+70)
}
no = int(input("lütfen ögrenci no giriniz : "))
print( "numaralı" + ogrenciler_isim[no] + "ismindeki öğrencinin yaşı " + ogrenciler_yas[no] + "ve not ortalaması" + ogrenciler_not[no] )
# eklentiler yapılacak 