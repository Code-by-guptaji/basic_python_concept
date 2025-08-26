a = input(" Write a string for perform the string operations: ")
age = 36

print("your given string is : " , a)
print("Length of the string is : " , len(a))
print("Uppercase of the dstring is : " , a.upper() )
print("Lowercase of the string is : " , a.lower())
print("Slicing of the first 4 character :" , a[:4])
print ("Slicing of the last 4 character :" , a[-5:])
print("Slicing of the string from 2 to 5 character :" , a[2:5])
print("your string after remove the extra white space is : " , a.strip())
print("your string after replace the 'a' with 'e' is : " , a.replace("a" , "e"))
print ("your string after seprate the words : " , a.split(" , "))
print (f"your age is : {age} years ")