n = int(input())
length = 0
while n > 0:
  n //= 10
  length += 1
print(length)

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
