tuple2 = (("çiçek", "böcek", "demet"))
tuple1 = tuple(("çiçek", "böcek", "demet"))
print(tuple2)
print(tuple1)
if "çiçek" in tuple2:
    print("ÇİÇEK VAR")
else:
    print("ÇİÇEK YOK")
x = ("merve", "azra","selen")
y = list(x)
y[1] = "sara"
print(y)