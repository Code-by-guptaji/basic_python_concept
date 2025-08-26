import re 

txt = "The rain in Spain"
x = re.search("^The.*Spain$",txt)

y = re.findall("ai" , txt)
print(y)

if y:
    print("Yes, there is at least one match!")
else:
    print("No match")

z = re.findall("portugal" , txt)

if z: 
    print("Yes, there is at least one match!")
else:
    print("No match")

a = re.split("\s" , txt)
print(a)

b = re.search("\s" , txt)
print("The first white space character is located in position : " , b.start())

c = re.sub("\s" , "9" , txt )
print(c)

d= re.sub("\s" , "9" , txt , 2)
print(d)