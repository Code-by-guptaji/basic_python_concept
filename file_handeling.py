f1 = open("demofile.txt")

# the code above is same as the following code:

f2 = open("demofile.txt", "rt")

print(f1.read())

# Using the with statement

with open("demofile.txt", "r") as f3:

    print(f3.read())

# for close the file 
f1.close()
f2.close()
f3.close()


# for Return the 5 first characters of the file:

with open("demofile.txt" ) as f4 :
    print(f4.read(5))

# You can return one line by using the readline() method:

    print(f4.readline())
    print(f4.readline())

    for x in f4:
        print(x)

f4.close()

# create a new file from here :

# f5 = open("myfile.txt","x")
f5 = open("myfile.txt","a")
f5.write("Hello Guys , you are welcome on my website")

f5 = open("myfile.txt","r")
print(f5.read())


# To delete a file, you must import the OS module, and run its os.remove() function:

import os
# os.remove("myfile.txt")  # for delete a file 
# os.rmdir("myfolder")  # for delte a folder