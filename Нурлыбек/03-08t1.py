n = [int(i) for i in input().split()]

print(len(n))
print(n[0])
print(n[6])
# 0 1 2 3 4 5 6 
for x in range(1,len(n)):
    if n[x]> n[x-1]:
        print(n[x])
