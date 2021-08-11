# 1 2 3 4 5 6 7
# 1 5 1 6 3 7 2

n = [int(i) for i in input().split()]

max = 0
i =1
while i<len(n):
    if n[i] > n[max]:
        max = i
    i+=1

print(n[max])

