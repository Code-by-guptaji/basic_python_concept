import mymodule as mx
from mymodule import greetings

mx.greetings("Ravi")

a = mx.person["Name"]
print(a)

# You can name the module file whatever you like, but it must have the file extension .py 

import platform

a =platform.system()
print(a)

b=dir(platform)
print(b)

