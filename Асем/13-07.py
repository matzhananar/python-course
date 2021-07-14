a = list(input().split())
#a = [int(i) for i in input().split()]

for x in range(0, len(a)):
    if int(a[x])%2 ==0:
        print(a[x])

