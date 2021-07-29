n = input()
# word -> Word

def capitalize(n):
    small =  n[0]
    big = ord(small)-32
    big = chr(big)
    return big+n[1:]

print(capitalize(n))