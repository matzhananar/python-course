min = 1000
inmin = 0

x = [int(i) for i in input().split()]

for i in range(0,len(x)):
    if x[i] < min:
        min = x[i]  
        inmin = i

print(min, inmin)