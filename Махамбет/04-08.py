#вывести элементы под четным индексом
n = list(input().split())

print(n[-1])    #последний элемент
print(len(n))   #длина массива

i = 0
while i<len(n):
    print(n[i], end=" ")
    i=i+2             # 0 1 2      #0 2 4 6 8