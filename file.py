with open("C:/Users/Анар/Desktop/python/hello.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)