max = -1000
inmax = 0

x = [int(i) for i in input().split()]

for i in range(0,len(x)):
    if x[i] > max:
        max = x[i]
        inmax = i

print(max, inmax)

