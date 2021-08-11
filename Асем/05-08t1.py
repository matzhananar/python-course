import re 
a = input()
def finder(a):
    pattern = 'ab{0}'
    if  re.search(pattern,a):
        return "there is a match"
    else:
        return "there is no match"

print(finder(a))