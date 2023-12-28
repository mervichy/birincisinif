gun = input("Doğum gününüzü girin:")
ay = input("ay:")
yil = input("yıl:")
print(f"{gun}.{ay}.{yil}")

if int(gun) >= 32:
    gun=input("gün yanlış tekrar:")
if int(ay) >= 13:
    ay=input("ay yanlış tekrar:")

gun1=0
if int(gun[0]) == int(gun[1]):
    gun1=int(gun[0])+int(gun[0])
else: 
    len(gun)==2
    gun1=int(gun[0])+int(gun[1])

ay1=0
if int(ay[1]) == int(ay[1]):
    ay1=int(ay[1])+int(ay[1])
else: 
    len(ay)==2
    ay1=int(ay[0])+int(ay[1])

yil1=0
if len(yil)==4:
    yil1=int(yil[0])+int(yil[1])+int(yil[2])+int(yil[3])

dg = gun1+ay1+yil1
dg2=0
dg1=str(dg)
dg2=int(dg1[0])+int(dg1[1])


if int(dg1[0]) == int(dg1[1]):
    dg2=int(dg1[0])+int(dg1[1])


if dg2 == 1:
    print("Sayınız ",dg2,"dir","1: Numeroloji sisteminde 1 sayısının anlamı; Bağımsızlık, yaratıcılık, kendine düşkünlük, ego olarak ifade edilir. Kişi hem kendine yeterli hem de tam bir liderdir. Yani liderliği temsil eder. İş yaşamında acelecilik, aşırılık ve hükmedici davranışlardan kaçınması kişi adına fayda sağlayabilir.")
elif dg2 == 2:
    print ("Sayınız ",dg2,"dir","2: Kişilik özellikler; bağımlılık, aşırı duyarlılık, kavrama ve tasarım, iş birlik anlayışı ve sezgi yeteneği gelişmiştir. Kişi sevgi dolu, eleştirici ve barış yanlısı, ideal ortaktır. Detaylara takılmaktan ve yalnızlıktan kaçınmalıdır.")
elif dg2 == 3:
    print ("Sayınız ",dg2,"dir","3: Numerolojide 3 rakamı; sosyal, arkadaş canlısı, sanata yatkın, iyimser, ziyankarlık, yüzeysellik anlamlarına gelir. Dışa dönük bir kişidir. Yaşamı ve eğlenceyi sever. Oldukça yaratıcı ve duyarlıdır. Rutini sevmez. Kendine disiplin uygulamayı benimsemesi gerekir.")
elif dg2 == 4:
    print ("Sayınız ",dg2,"dir","4: Numerolojide 4 sayısı sağlam, pratik, uygulayıcı, bükülmez ve sıkı bir çalışan anlamına gelir. Her konuda başarıyı yakalamak ister. Candan ve iyi bir arkadaş olma konusunda yardıma ihtiyacı vardır. Aşırı güvenlik duygusuna kapılmamalıdır.")
elif dg2 == 5:
    print ("Sayınız ",dg2,"dir","5: Özgürlük, gezginlik, uyum kabiliyeti, değişkenlik gibi karakteristik özellikler numerolojide bu rakamın karşılığı olarak bilinmektedir. İkna edici bir kişiliğe sahiptir ve cesur bir kişiliktir. Can sıkıntısı olumsuz etkiler. Amacından kolayca sapması söz konusudur.")
elif dg2 == 6:
    print ("Sayınız ",dg2,"dir","6: Anlayış, aşk, sorumluluk, kıskançlık, her işe müdahale etmek gibi özelliklere sahiptir. Oldukça sıcak, koruyucu ve mutlu bir kişiliğe sahiptir. Sevdikleri için fedakarlık yapmaktan çekinmez. Sağlam ve güvenilir bir yapısı bulunur. Kendini kötümser bir ruh haline sokmaktan ve başkaları tarafından istismar edilen duygularından arınmış olmalıdır.")
elif dg2 == 7:
    print ("Sayınız ",dg2,"dir","7: Bu rakam; sır saklama, zeka, ruhsallık ve baskıcılığı ifade eder. Düşünür bir kişiliğe sahiptir. Değişken ve eksantriktir. Mesafeli ve soğuk olmaktan kaçınmalıdır. Ayrıca iyi şeylere sahip olmama duygusu ve yalnızlıktan kaçınmalıdır.")
elif dg2 == 8:
    print ("Sayınız ",dg2,"dir","8: Organizasyon yeteneğine sahip, güçlü, yönetici ruha sahip ve oldukça adildir. Sonuca giden bir kişiliğe sahiptir. Bu bağlamda her zaman kararlı ve güçlü yapısı ile ön plana çıkmaktadır. Özellikle maddi konularda başarılıdır. Hedefinin karşısında gördüğü kişilere karşı duygusuzca davranmaktan kaçınması gerekir.")
elif dg2 == 9:
    print ("Sayınız ",dg2,"dir","9: Hümanist, romantik, şefkatli, duygusal, sanatkar, sezgili, duyarlı, yaratıcı ve konforuna düşkündür. Kendini anlatmak adına tüm dünya ile savaşabilir. Kötü alışkanlıklarından arınmak ve yaşamın küçük detaylarından olumsuz etkilenmemek adına gayret göstermesi gerekir.")
elif dg2 == 11:
    print ("Sayınız ",dg2,"dir","11: Duyarlı, fanatik ve sezgi gücü yüksektir. Ayrıca keşif yeteneğine sahiptir. Öngörülü ve hayalci bir kişiliğe sahiptir. Bilinç üstü gelişmiştir ve sanatkardır. Aşırı duyarlılık ve gerginlik halinden uzak durmalıdır.")
elif dg2 == 22:
    print ("Sayınız ",dg2,"dir","22: Numerolojide 22 rakamının anlamı; maddi alanda üstün, zenginliğe kolay ulaşabilen, oldukça pratik bir idealist olarak tanımlanır. Amacına doğru ilerler ve eli çabuktur. Düşünce tarzı globaldir. Geleceğe fazla düşünmekten kaçınmalıdır.")