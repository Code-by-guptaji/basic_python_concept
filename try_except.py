try:
    print(x)  # x is not defined
except :
    print("An error occured")


try:
    print(y) # y is not defined
except NameError:
    print("Variable y is not defined")
except:
    print("Something else went wrong")


try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

try: 
    print(z)  # z is not defined
except: 
    print("Something went wrong")
finally:
    print("The try except is finished")



try:
   f = open("demofile.txt")
   try:
       f.write("Hello World")
   except:
        print("Something went wrong when writing to the file")
   finally:
     f.close()
except:
   print("Something went wrong when opening the file")


# Raise an error and stop the program if x is lower than 0:

m = -1
if m < 0:
    raise Exception("Sorry , no numbers below zero")

# Raise a TypeError if x is not an integer:

n = "hello"

if not type(n) is int :
    raise TypeError("Only integers are allowed")