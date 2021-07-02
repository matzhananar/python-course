n  = int(input())# n = 7
sum = 0

for x in range(1, n+1):
    t = x**2        # t = 1**2        t = 2**2          t = 3**2
    sum = sum + t   # sum = 0 + 1     sum = 1 + 4       sum = 5 + 9
    print(sum)      

print("результат",sum)
