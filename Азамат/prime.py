n = int(input())

def Isprime(n):
    i = 2
    while n%i != 0:
        i +=1
    return i == n


print(Isprime(n))