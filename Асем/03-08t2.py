n = [int(i) for i in input().split()]
price = 49.1234567
weight = 12
txt = "Tomato costs {:.2f} dollars and weights {} pounds"
print(txt.format(price,weight))

n.sort()
print(n)
print(f"maximum number is {n[-1]}")