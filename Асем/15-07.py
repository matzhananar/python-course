n = [int(i) for i in input().split()]

counter = 0

for x in range(1,len(n)):
    if n[x] > n[x-1]:
        counter+=1

print(counter)