adsoyadList = []
while True:
    adsoyad = input("Adınız soyadınız:")
    if not adsoyad:
        break
    adsoyadList.append(adsoyad)
print(adsoyadList,"girilen adlar")
for adsoyad in adsoyadList:
    print(adsoyad)