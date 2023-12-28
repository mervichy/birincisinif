x = ("elma","armut","çilek")
y = list(x)
y.append("ananas")
x = tuple (y)
print(x)

m = ("elma","armut","çilek")
n = ("muz",)
m += n
print(m)

meyveler = ("elma","armut","çilek")
(yesil, sari, mavi) = meyveler
print(yesil)
print(sari)
print(mavi)