a = int(input())
n = int(input())

def power(a,n):
    pow= 1
    for x in range(abs(n)):
        pow = a*pow
    if n>0:
        return pow
    else:
        return 1/pow

print(power(a,n))



