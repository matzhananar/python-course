n = int(input())
k = int(input())
sum = 1
x = 1

for i in range(1, k+1):
    x = x*n
    sum = sum+x

print(sum)