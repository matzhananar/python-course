a = int(input())
n = int(input())

def xor(a,n):
    if (a == 1 and n ==0) or (a==0 and n==1):
        return 1
    else:
        return 0

print(xor(a,n))