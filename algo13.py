#1'den 5'e kadar sayı yazdır, istenilen sayıyı ekrana getiren kod
list = []
for x in range(5):
    sayi=input("1'den 5'e kadar sayı girin:")
    list.append(sayi)
print(list)
kac=input("kaçıncı sayıyı istiyorsun?")
print(list[int(kac)])