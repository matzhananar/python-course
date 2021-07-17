a = int(input())
b = int(input())
c = int(input())
d = int(input())

def minn(a,b,c,d):
    mass = [a,b,c,d]
    mass.sort()
    print(mass)
    print(mass[0])

minn(a,b,c,d)
