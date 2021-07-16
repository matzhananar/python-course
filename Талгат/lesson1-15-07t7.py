n = int(input())
a = int(input())

if a>0 and n>0:
    print("positive numbers")
elif a<0 or n<0:
    print("один из них отрицательное число")
elif not a>n:
    print("n больше чем а")
