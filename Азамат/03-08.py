from re import findall


try:
    print(x)
except:
    print("error")
else:
    print("there is no exception")
finally:
    print("try except is finished")

n = input()
x = findall('^\d\d\d\d\d\d\d\d\d\d\d',n)

if x ==[]:
    raise TypeError

