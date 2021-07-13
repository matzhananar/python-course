thisdi ={
    "brand" : "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2000,
    "sold": 2000
}

x = thisdi['model']
print("model",x)

y = thisdi.get("model")
print("model",y)

z = thisdi.keys()
print("keys",z)


thisdi["color"] = "white"
print("key",z)
print(thisdi)

print(len(thisdi))
print(type(thisdi))

x = thisdi.items()
print(x)

if "modl" in thisdi:
    print("yes there is")
else:
    print("there is no model")

thisdi["year"] = 1990
print(thisdi)
thisdi.update({"year": 2020})
print(thisdi)
thisdi.update({"price": "2000$"})
print(thisdi)

