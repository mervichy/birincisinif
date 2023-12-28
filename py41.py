dgun = input("lütfen soğum gününü gir")
while True:
    if len(dgun)<2:
        dgun = input("dgnün bAŞINA 0 EKLE")
    elif int(dgun)>31:
        dgun = input("Yanlış girdin tekrar :")

    else:
        break
day = input("lütfen soğum ay gir")
while True:
    if int(day)>12:
        dgun = input("Yanlış girdin tekrar :")
    if len(day)<2:
        dgun = input("dgnün aYIn bAŞINA 0 EKLE")
    else:
        break
dyil = input("lütfen soğum yilini gir")
while True:
    if int(dyil)<1950 or int(dyil)>2023:
        yil = input("Yanlış girdin tekrar :")
    else:
        break

dgun1 = int(dgun[0]) + int(dgun[1])
day1 = int(day[0]) + int(day[1])
dyil1 = int(dyil[0])+ int(dyil[1]) + int(dyil[2]) + int(dyil[3])

genel = dgun1 + day1 + dyil1
strgenel = str(genel)


if genel==1:
    print(genel)
elif genel==2:
    print(genel)
if genel==3:
    print(genel)
if genel==4:
    print(genel)
if genel==5:
    print(genel)
if genel==6:
    print(genel)
if genel==7:
    print(genel)
if genel==8:
    print(genel)
if genel==9:
    print(genel)
if genel==11:
    print(genel)
if genel==22:
    print(genel)
else:
    if genel>9 and genel !=11 or genel>9 and genel!=22:
        yeni = int(strgenel[0]) + int(strgenel[1]) 