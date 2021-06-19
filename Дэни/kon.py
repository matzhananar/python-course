a = int(input())
b = int(input())
c = int(input())
d = int(input())

k = a-c
l = b-d

if(k<0): 
    k=-k
if (l<0):
    l=-l

if((k==2 and l==1) or (k==1 and l==2)):
    print ("YES")
else:
    print("NO")
     
