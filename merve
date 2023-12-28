# kullanıcının girdiği bir yazı üzerinde temizlik yapacak fonksiyon tanımlanacak algoritma içinde ilgili fonksiyon çağırılarak
# temiz hali yazılacak 1den fazla boşluk temizlenecek 1 den fazla  ,,  noktalama işaretleri yan yana ise teke indirilecek

def temizleme():
    tirnak=(metin.count(";"))-1
    metin2=metin.replace(";","",tirnak)
    soruisareti=(metin2.count("?"))-1
    metin2=metin2.replace("?","",soruisareti)
    nokta=(metin2.count("."))-1
    metin2=metin2.replace(".","",nokta)
    metin3=metin2.strip("  ")
    print(metin3)

# yazılan metinin ;;;; saçmalarını      temizleme ??

metin=input("metin giriniz:")

temizleme()