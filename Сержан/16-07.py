n = int(input())

fibsum = 0
fib1 = -1
fib2 = 1
i =-1

while i<n:
    fibsum = fib1 + fib2
    i +=1
    fib1 = fib2
    fib2 = fibsum
    print(i, fibsum)
print(fibsum)