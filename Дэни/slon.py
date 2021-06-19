a = int(input())
b = int(input())
c = int(input())
d = int(input())

k = a-c
l = b-d

if k<0:
    k=-k

if (l<0):
    l=-l

if(k==l):
    print("YES")
else:
    print("NO")
