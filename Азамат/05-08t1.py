import re
n = input()

t = re.search("ab*", n.start())
print(t)