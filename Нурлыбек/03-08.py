n = [int(i) for i in input().split()]

# n[x] это сам элемент под индексом x
# x это индес в массиве
# i = 0 1 2 3 4 5

i =0
while i<len(n):
    if n[i] %2 ==0:
        print(n[i], end=" ")
    i+=1

