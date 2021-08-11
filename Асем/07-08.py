n = int(input())

sat = open("C:/Users/Анар/Desktop/python/Асем/sat.txt","w")
hello = open("C:/Users/Анар/Desktop/python/Асем/hello.txt","r")
array = hello.read().split()

for word in array:
    sat.write(array[word])

sat.close()