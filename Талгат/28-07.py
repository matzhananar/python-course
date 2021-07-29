n = int(input())

def isPrime(n): # 3 5 7 11 13
    d = 2
    while n % d != 0:    # 13 % 2 != 0   d + 1 = 3  # 13 % 3 != 0  d +1
        d+=1             # 12 % 2 == 0   d ==2
    return d == n

print(isPrime(n))