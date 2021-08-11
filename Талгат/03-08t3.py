n = int(input())


def fibbon(n):
    f1 = 1
    f2 = 1
    fsum = 0
    for x in range(fsum,n):
        fsum = f1+f2
        f1 = f2
        f2 = fsum
        print(fsum, x)

fibbon(n)
        