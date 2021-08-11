n = int(input())
txt = open("C:/Users/Анар/Desktop/python/Азамат/hello.txt", "r")
array = txt.readlines()

for x in range(1,4):
    print(array[-x])