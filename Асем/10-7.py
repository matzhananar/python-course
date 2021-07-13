n = int(input())
prod = 2
sum = 1

for x in range(1, n+1):
    prod = 1/(x*prod)
    sum = sum+prod

print(sum)