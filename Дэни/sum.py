n = int(input())
k = 0
cnt =0

for i in range(n+1):
    k = i**2
    cnt = k+cnt

print(cnt)

