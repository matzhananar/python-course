x = int(input())
b = int(input())
z = int(input())
if x>b and x>z:
    print("самый большой цифр", x)
elif b>x and b>z:
    print("самый большой цифр", b)
elif x == b and b == z:
    print("barlygu ten")

else:
    print("самый большой цифр", z)

