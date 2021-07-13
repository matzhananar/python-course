def capitalize(word):
    small = word[0]
    big = chr(ord(small) - ord('a') + ord('A'))
    return big + word[1:]
 
source = input().split()
res = []
for word in source:
    res.append(capitalize(word))
print(' '.join(res))