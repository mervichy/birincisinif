#değişken tanımladık
el=100
ar=150
dom=200
pat=175
para = int(input("Para giriniz"))
tur = input("Ne alacaksın?")
kg = int(input("Kaç kilo?"))
kalan=0 # sonradan kalanı print ettiğimizde görünmesi için sıfıra eşitledik
if para<100:
    print("Paranız yetersiz.")
elif tur=="elma":
    harcanan=el*kg
    kalan=para-harcanan
    if kalan<0:
        print("Paranız yetmedi.")
elif tur=="armut":
    harcanan=ar*kg
    kalan=para-harcanan
    if kalan<0:
        print("Paranız yetmedi.")
elif tur=="domates":
    harcanan=dom*kg
    kalan=para-harcanan
    if kalan<0:
        print("Paranız yetmedi.")
elif tur=="patates":
    harcanan=pat*kg
    kalan=para-harcanan
    if kalan<0:
        print("Paranız yetmedi.")
print("Kalan paranız " , kalan)
