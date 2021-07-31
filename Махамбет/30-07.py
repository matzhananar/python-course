n = int(input())
i = 1
q = 2
while i<=n:
    while q<=i:
        if i%q != 0:
            q=q+1
        q+=1
    if q ==i:
        print(q)
    i +=1
    