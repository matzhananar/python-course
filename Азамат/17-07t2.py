# условие1 or условие2 -> 1 1 -> 0 1 -> 1 0      0 0
# условие1 xor условие2 -> 0 1 -> 1 0            0 0   1 1
# условие1 and условие2 -> 1 1                   0 0   1 1  0 1

x = int(input())
y = int(input())

def xorr(x,y):
    if (x == 1 and y == 0) or (x == 0 and y == 1):
        return 1
    else:
        return 0

print(xorr(x,y))

print(1<0)