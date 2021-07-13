numb = list(input().split())
print(numb[-1])

for x in range(0, len(numb)):
    if x%2 ==0:
        print(numb[x])
        