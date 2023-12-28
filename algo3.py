toplam=1
sayi = input('Sayı giriniz: ')
while sayi != "e":
    toplam= toplam * int(sayi)
    sayi = input('Sayı giriniz: ')
print(toplam)