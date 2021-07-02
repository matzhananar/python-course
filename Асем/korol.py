a = int(input("координаты короля по строке     "))
b = int(input("координаты короля по столбцу    "))

c = int(input("координаты фигуры по строке    "))
d = int(input("координаты фигуры по столбцу   "))

k = a-c
l = b-d

if k < 0:
    k = -k

if l<0:
    l = -l

if k<=1 and l<=1:
    print("yes")
else:
    print("no")