#n = (int(i) for i in input().split())
n = list(input().split())

for x in range(0,len(n)):
    n[x] = int(n[x])
    if n[x]%2 == 0:
        print(n[x])


