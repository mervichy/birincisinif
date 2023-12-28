sayi=int(input("sayi giriniz"))
liste=[]
liste.append(1)
liste.append(1)
for x in range(2,sayi):
    liste.append(liste[x-2]+liste[x-1])
print(liste)