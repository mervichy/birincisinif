#öğrencinin girdiği vize notunun %40ını final notunun %60ını hesaplayan ve finalden 50nin altında not almış ise kaldınız, not ortalaması 60 ve üzeri ise geçtiniz yazan algoritmayı yazınız.
vize=int(input("vize notunuzu girin:"))
final=int(input("final notunuzu girin:"))
ortalama=(vize*0.4)+(final*0.6)
print(ortalama)
if final<50:
    print("Kaldınız.")
    elif ortalama(<)