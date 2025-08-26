import json



#  JOSN to python 

x = '{"name" : "Ravi" , "age" : 21 , "city" : "delhi"}'

y = json.loads(x)

print(y)
print(y["name"])

# PYTHON to json

z = {
    "name" : "Ravi" , 
    "age":21 , 
    "city" : "Bombay"
}

a = json.dumps(z)
print(a)


#  Convert Python objects into JSON strings, and print the values:

print(json.dumps({"name":"Ravi" , "age": 31 , "city":"Kolkatta"}))
print(json.dumps(["apple" , "banana" , "cherry"]))
print(json.dumps(("apple" , "banana" , "cherry")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))



p = {
    "Name:" : "Ravi" ,
    "age" : 21  , 
    "married" : False , 
    "pets" : None , 
    "cars" : [
        {"model" : "BMW"  , "mpg" :27.5}, 
        {"model" : "ford" , "mpg" :24.1}
          ]
}

o = json.dumps(p)
print(0)



x = {
    "name": "Ravi",
    "age": 21,
    "city": "Delhi"
}

# formatted JSON
y = json.dumps(x, indent=4, separators=(". ", " = "))
print(y)
