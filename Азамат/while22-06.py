i = 0

while i<6:
    print(i)
    i+=1 #i=i+1

n = int(input())
length = 0

while n>0:
    n//=10 #n = n // 10
    length+=1

print(length)
    
x = 0

while x <6:
    x += 1
    print(x)
    if x ==4:
        break
    
    
    y = 0

while y<6:
    y+=1
        
    if y ==3:
        continue
    else:
        print("y is more than 6")
    print(y)
    


