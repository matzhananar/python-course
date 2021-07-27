x = int(input())
y = int(input())
counter =1 
while x<=y:
    x = x + x*0.1
    counter += 1

print(counter)