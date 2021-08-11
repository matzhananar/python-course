import re 
txt = "The rain in Spain"

x = re.search("Spain$",txt)
print(x)

x = re.findall("ai",txt)
print(x)

x = re.search("\s", txt)
print("the probely",x.start())

x = re.split("\s",txt)
print(x)

x = re.sub("\s"," : ", txt)
print(x)
