slonx = int(input("Введите координаты слона по х: "))
slony = int(input("Введите координаты слона по y: "))

figurex = int(input("Введите координаты фигуры по х: "))
figurey = int(input("Введите координаты фигуры по y: "))

if slonx-figurex<0:
    slonx-figurex= (slonx-figurex)*-1

if slony - figurey<0:
    slony-figurey = (slony-figurey)*-1


if (slonx-figurex) == (slony-figurey):
    print("yes")
else:
    print("no")
