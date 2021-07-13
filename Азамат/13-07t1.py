n = list(input().split())
sum = 0
for x in range(0,len(n)):
    if int(n[x])>0:
        sum = sum+1

print(sum)