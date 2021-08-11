x = int(input())
p = int(input())
y = int(input())

counter = 0
while x<=y:
    x = x + x*(p/100)
    x = int(x)
    counter+=1
    print(x, counter)