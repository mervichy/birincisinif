sifre = "MERVE"
password=input("Şifre Giriniz")
while password !="":
    if password.upper() == sifre.upper() :
        print("Girişiniz onaylanmıştır.")
        break
    else:
        print ("Şifreniz yanlıştır.")
        password=input("Şifre Giriniz")