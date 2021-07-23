n = int(input())

def fib(n):
    f1 = -1
    f2 = 1
    i = 0
    while i<n:
        sum = f1+f2
        f1 = f2
        f2 = sum
        i +=1
        print(i, f2)
fib(n)