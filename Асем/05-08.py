import re

a = input()
#txt = re.compile(r'[a-zA-Z0-9.]')
find = re.search("[a-z]",a)
print(find.start())