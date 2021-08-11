n = list(input().split())
print(n)

x = 0
while x < len(n):
    n[x] = int(n[x])

print(n)