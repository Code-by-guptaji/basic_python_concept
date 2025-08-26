# A variable created inside a function is available inside that function:
def myfun():
 x = 5
 print(x)
myfun()

# The local variable can be accessed from a function within the function:
def function():
  x= 300
  def innerfunction():
    print(x)
  innerfunction()   

function()


# A variable created outside of a function is global and can be used by anyone:

a = 500
def define():
    print(a)

define()

# If you create a variable with the same name inside a function, this variable will be local and can only be used inside the function.

b = 500
def show():
   b=300
   print(b)

show()
print(b)


c = 300

def myfunc():
  global c
  c = 200
  print(c)

myfunc()

print(c)

# If you use the nonlocal keyword, the variable will belong to the outer function:

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())