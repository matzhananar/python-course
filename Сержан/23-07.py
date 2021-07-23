a = list(input().split())
print(len(a))

for x in range(0,len(a)):
    a[x]=int(a[x])-1

print(a)