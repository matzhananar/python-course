a = int(input())
b = int(input())
c = int(input())
d = int(input())

def min(a,b,c,d):
    massive = [a,b,c,d]
    massive.sort()
    print(massive[0])

min(a,b,c,d)