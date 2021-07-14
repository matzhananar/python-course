n = list(input().split())

a = 0

for x in range(0, len(n)):
    if int(n[x]) > a:
        a = n[x]
    
print(a)