class Person:
    def __init__ (self , fname , lname ):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname , self.lastname)

x = Person("Himesh" , "kumar")
x.printname()

class Student(Person):
    pass

x = Student("Vedant" , "Gupta")
x.printname()