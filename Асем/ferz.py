a = int(input("координаты ферзя по строке     "))
b = int(input("координаты ферзя по столбцу    "))

c = int(input("координаты фигуры по строке    "))
d = int(input("координаты фигуры по столбцу   "))

k = a-c
l = b-d

if k < 0:
    k = -k

if l<0:
    l = -l

if (a == c or b == d) or k == l:
    print("Ферзь бьет фигуру")
else:
    print("Ферзь не бьет фигуру")