n = int(input())

def isPrime(n):
    i = 2
    while n%i != 0:
        i +=1
    return i == n

print(isPrime(n))

