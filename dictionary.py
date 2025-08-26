dict = {
    "name" : "ravi",
    "age" : 21 , 
    "cse" : True
}

print(dict)
print(len(dict))
print(type(dict))

x = dict.keys()
print(x)

y = dict.values()
print(y)

z = dict.items()
print(z)


dict["age"]=22
print(dict)

dict.update({"age":24})
print(dict)

dict["batch"] = 2027
print(dict)

dict.pop("cse")
print(dict)

dict.popitem()
print(dict)

del dict['name']
print(dict)

# del dict # it can also delete the entire dictionary completely

# dict.clear()
# print(dict)

for x in dict:
    print(x)

for x in dict.values():
    print(x)

for x , y in dict.items():
    print(x,y)

dict1 = dict.copy()
print(dict1)


myfamily = {
    "child1":{
        "name":"Emil"
    
        ,"year":2004}
    ,"child2":{
        "name":"Tobias"
        ,"year":2007}
}

print(myfamily)