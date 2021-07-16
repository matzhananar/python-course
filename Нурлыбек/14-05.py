lx = int(input())
ly = int(input())

fx = int(input())
fy = int(input())

coo1 = fx - lx
coo2 = fy - ly

if coo1<0:
    coo1 = -coo1

if  coo2<0:
    coo2 = -coo2

#slon  -> 4 4
#figu1 -> 6 2   2 -2
#figu2 -> 5 5   1  1
#figu3 -> 5 3   1 -1
#figu4 -> 7 1   3 -3
#figu5 -> 3 3  -1 -1

if coo1 == coo2:
    print("бьет")
else:
    print("не бьет")








