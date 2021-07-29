a = int(input())
n = int(input())

def power(a,n):
    p = 1
    for x in range(abs(n)):
        p = a*p
    if n<0:
        return 1/p
    else:
        return p

print(power(a,n))
    