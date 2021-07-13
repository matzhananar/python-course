n = list(input().split())
print(n[-1])

for x in range(0, len(n)):
    if x%2 == 0:
        print(n[x])
