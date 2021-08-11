import re 
txt = input()
def findall(txt):
    f = re.findall("ab{2,3}", txt)
    if len(f) !=0:
        return True
    else:
        return False

print(findall(txt))