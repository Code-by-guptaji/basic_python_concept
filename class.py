class myclass:
    x = 5

p1 = myclass.x
print(p1)

class person:
    name = "Himesh"
    age = 20

p2 = person.name
print(p2)


class Student:
    def __init__ (self , name ,age):
        self.name = name 
        self.age = age

p3 = Student("himesh" , 20)

print(p3.name)
print(p3.age)


class Employee:   
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"hello my name is {self.name} and I am {self.age} years old"
    
p4 = Employee("himesh", 20)   
print(p4)   



class Car :
    def __init__ (mysilyobject , name , model):
        mysilyobject.name = name
        mysilyobject.model = model
    
    def show(abc):
        print(f"car name is {abc.name} and model is {abc.model}")

c1 = Car("BMW" , 2020)
c1.show()

# del c1.show  # for delete the property of the object
# del c1 # for delete the 

# pass is used for define the class without any property