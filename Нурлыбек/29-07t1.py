x = int(input())
p = int(input())
y = int(input())

counter = 1

while x<=y:
    x += int(x*(p/100))
    counter+=1
    print(x,counter)