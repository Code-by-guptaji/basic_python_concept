list1 = ["hello" , "ravi" , 9 , 10.5 , True]

print("your list is : " , list1)
print("length of your list is :" , len(list1))
print("first element of your list is : " , list1[0])
print(type(list1))
print("last threen element of the list id : " , list1[-3:])

if "ravi" in list1:
    print ("yes , 'ravi' is in the list ")

list1[0] = "World"
print("Now updated list is : " , list1)

list1.insert(2 , "python")
print("Now updated list is : " , list1)

list1.append("c++")
print("Now updated list is : " , list1)


list2 = ["java" , "c" , "ruby" , "cloud"]
list1.extend(list2)
print("Now updated list is : " , list1)

list1.remove("c++")
print("Now updated list is : " , list1)

list1.pop(2)
print("Now updated list is : " , list1)

list1.pop()
print("Now updated list is : " , list1)

del list1[0]
print("Now updated list is : " , list1)

# del list1  # for deleting the entire list

# list1.clear()
# print("Now updated list is : " , list1)


list3 = [11,22,33,54,12,32,44,64,25, 24]

list3.sort()
print("Sorted list is : " , list3)

list3.sort(reverse=True)
print("Reverse sorted list is : " , list3)


list4 = list2.copy()
print("Copied list is : " , list4)

list5 = list1 + list2
print("Concatenated list is : " , list5)

