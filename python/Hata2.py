liste = ["1","3","5","20b","abc","10a","60"]
for x in liste:
    try:
        sonuc = int(x)
        print(sonuc)
    except ValueError:
        continue    