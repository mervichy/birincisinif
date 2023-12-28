def islem():
    kuvvet=0
    x=int(input("sayı giriniz:"))
    for i in range(1,x+1):
        kuvvet=kuvvet + i**i
    print(kuvvet)

islem()