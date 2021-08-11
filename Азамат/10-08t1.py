# r w a
x = open("C:/Users/Анар/Desktop/python/Азамат/hello.txt", "r")
print(x.read())
x.close()
x = open("C:/Users/Анар/Desktop/python/Азамат/hello.txt", "a")
x.write("more tetx please")
x.close()
x = open("C:/Users/Анар/Desktop/python/Азамат/hello.txt", "r")
print(x.read())
