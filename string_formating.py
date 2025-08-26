# print dynamic variable in the give string
a = 35
print(f"the value of a  is {a}")

# display value with 2 decimal
b = 12.464737
print(f"the value of b  with two decimal is {b:.2f}")


# perform operation in f string
print(f"the addition of 5 and 6 is {5+6}")

# add taxes before displaying the price 
price = 100
tax = 0.18
print(f"the price is {price} and price after the tax is {price + price*tax}")

#Return "Expensive" if the price is over 50, otherwise return "Cheap":
a = 51
comment = f"The item is {'Expensive' if a>50 else 'cheap'}"
print(comment)

# Executes function in the f-string
fruit = "apple"
print(f"I love {fruit.upper()}") 

# Call the function in f-string
def toconvertfeetintometer(feet):
    return feet*0.3048
print(f"the value of 10 feet in meter is {toconvertfeetintometer(10)}")

# use a comma as a thousand separator
num = 59993000
print(f"The pupulation of the city is {num:,}")



# => Before Python 3.6 we used the format()
txt = "the price is :{}"
print(txt.format(100))


quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))


age = 36
name = "John"
info = "my name is {1} and my age is {0}"
print(info.format(age, name))

# use a Named Indexes

myorder = "I buy a car of {carname} for {price} rupey"
print(myorder.format(carname="Range Rover" , price = 10000000))