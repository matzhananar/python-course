import re
try:
    print("hello")
except:
    print("error")
else:
    print("there is no problem occured")
finally:
    print("Try except function worked")


txt = input()
x = re.findall("\d\d\d\d\d\d\d\d\d\d\d",txt)

if x ==[]:
    raise Exception("Sorry ur code is usefull")
else:
    print("perfect number")

x = input()
if not type(x) is int:
    raise TypeError