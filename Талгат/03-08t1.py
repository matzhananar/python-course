# and 1 1
# or  1 1   1 0   0 1
# xor 1 0   0 1

x = int(input())
y = int(input())

def xor(x,y):
    if (x==1 and y ==0) or (x ==0 and y ==1):
        return 1
    else:
        return 0

print(xor(x,y))