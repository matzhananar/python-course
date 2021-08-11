x = int(input())
y = int(input())
z = int(input())

def election(x,y,z):
    return (x+y+z>1)

if election(x,y,z) == True:
    print(1)
else:
    print(0)

