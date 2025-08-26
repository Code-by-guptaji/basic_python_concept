tuple1 = ("ravi" , "kiran" , "Niyyu" , "bhavana" , 1 ,2 ,3 ,4)

print(len(tuple1))
print(tuple1[0])
print(type(tuple1))
print(tuple1[:4])

# convert tuple into list

list1 = list(tuple1)
print(list1)

list1.remove("ravi")

tuple2 = tuple(list1)
print(tuple2)

tuple3 = tuple1 + tuple2
print(tuple3)