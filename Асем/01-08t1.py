import re
x = input()

z= re.findall("\d", x)
print(z)


t = int(input())
q = re.findall("\w", t)
print(q)
