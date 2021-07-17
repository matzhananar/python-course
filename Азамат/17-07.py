word = input()
#print(word[0])

def capitalize(word):
    first = word[0]
    cap = (ord(first)-32) #119
    cap = chr(cap)        # W
    return cap + word[1:]

print(capitalize(word))