n = int(input())

def fibbon(n):
    fibsum = 0
    fib1 = -1
    fib2 = 1
    for x in range(0,n+1):
        fibsum = fib1 + fib2
        fib1 = fib2
        fib2 = fibsum
    return fibsum

print(fibbon(n))
