sayi=int(input("sayı girin:"))
sayi1=1
sayi2=1
print(sayi1)
print(sayi2)

for x in range (1,sayi+1):
    sayi3=sayi1+sayi2
    if sayi3>sayi:
        break
    print(sayi3)
    sayi1=sayi2
    sayi2=sayi3
    