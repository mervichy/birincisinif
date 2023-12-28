sayi1 = input("1sayı giriniz:")
if sayi1=="":
    sayi1 = input(" lütfen sayı giriniz:")
sayi2 = input("sayı giriniz:")
if sayi2=="":
    sayi2 = input("sayı giriniz:")
sayi3 = input("sayı giriniz:")
if sayi3=="":
    sayi3 = input("sayı giriniz:")
sayilar = [sayi1 , sayi2 , sayi3 ]

isim1 = input("isim giriniz:")
if isim1=="":
    isim1 = input("isim giriniz:")
isim2 = input("isim giriniz:")
if isim2=="":
    isim2 = input("isim giriniz:")
isim3 = input("isim giriniz:")
if isim3=="":
    isim3 = input("isim giriniz:")
isimler = [isim1 , isim2 , isim3]
for x in sayilar:
    for y in isimler:
        print (x, y)