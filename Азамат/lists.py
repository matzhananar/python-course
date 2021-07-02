thislist = ["apple", 1234, "saturday", 12345]
print("the length is",len(thislist))

print("2nd element is",thislist[2])

print(thislist[0])

list1 = ["hello", [1,2,3,4], 1234, "world"]
print(list1)


qwe = [0,1,2,3,4,5,6,7,8,9,10]

print(qwe[2:5])
print(qwe[-5])
print(qwe[:-5])


odd = [2,4,6,8]
print("list odd",odd)

odd[0] = 1

print("list odd",odd)

odd[1:4] = 3,5,7
print("list odd",odd)


odd = [1,3,5]

odd.append(7)
print("append of list",odd)

odd.extend([9,11,13])
print("extend of list", odd)

plus = ["monday","tuesday","wednesday"]
second = [1,2,3]
print(plus+second)

odd.insert(1,3)
print(odd)

odd[2:3] = [10,12,14]
print(odd)

del odd[2]
print(odd)

del odd[1:8]
print(odd)

del odd
print(odd)