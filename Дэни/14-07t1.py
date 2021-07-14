n = [int(i) for i in input().split()]

counter = 0

for x in range(0, len(n)):
    if n[x] > 0:
        counter+=1
    
print(counter)
