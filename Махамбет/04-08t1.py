n = list(input().split())

i =0
while i<len(n):
    n[i] = int(n[i])

    if n[i]%2 == 0:
        print(n[i], end=" ")
        i+=1