x = int(input())
y = int(input())

def task1(x,y):
    if (x == 1 and y == 0) or (x ==0 and y==1):
        return 1
    else:
        return 0

print(task1(x,y)) 