a = input()
b = input()

if (a =="банан" or b == "молоко") or (b =="банан" or a == "молоко"):
    print("мы сделаем коктейль")
elif (a == "мука" and b =="яйцо") or (b == "мука" and a =="яйцо"):
    print("пирогу быть")
else:
    print("мы не сделаем ни пирог ни коктейль")


