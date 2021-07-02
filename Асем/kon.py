a = int(input("координаты коня по строке       "))
b = int(input("координаты коня по столбцу      "))

c = int(input("координаты фигуры по строке     "))
d = int(input("координаты фигуры по столбцу    "))

k = a-c
l = b-d

if k < 0:
    k = -k

if l<0:
    l = -l

if (k == 1 or k == 2) and (l == 1 or l ==2):
    print("yes")
else:
    print("no") 