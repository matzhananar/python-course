n = int(input())
k = int(input())

j =1
o = 1
l = 1

for i in range(n+1):
    j*=i

for i in range(k+1):
    o*=i

for i in range(k-n):
    l*=i

x = j/(o*l)
print(x)