# 1 2 3 4 5 6 = 5

a = [int(i) for i in input().split()]

counter = 0

for x in range(1, len(a)):
    if a[x] > a[x-1]:
        counter+=1

print(counter)

