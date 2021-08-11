
f = open("C:/Users/Анар/Desktop/python/Азамат/hello.txt", "a")

f.write("Now the file has more content!")
f.close()

f = open("C:/Users/Анар/Desktop/python/Азамат/hello.txt", "r")
print(f.read())
