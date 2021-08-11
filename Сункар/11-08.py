ferzx = int(input("Введите координаты ферзя по х: "))
ferzy = int(input("Введите координаты ферзя по y: "))

figurex = int(input("Введите координаты фигуры по х: "))
figurey = int(input("Введите координаты фигуры по y: "))

k = ferzx-figurex
l = ferzy - figurey

if k<0:
    k = k*-1
if l<0:
    l = l*-1

if ferzx == figurex or ferzy == figurey or (k == l):
    print("Да ферзь бьет данную фигуру")
else:
    print("Нeт ферзь не бьет данную фигуру")