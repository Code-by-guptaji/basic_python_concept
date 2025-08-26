set1 = {"hello" , "banana" , "orange" , 1 , 3, 5}
set2 = {"go" , "went" , "gone"} 
list1 = ["forward", "go" , "get"]
print(set1)
print(type(set1))

for x in set1:
    print(x)

print("banana"  in set1)
print("hello" not in set1)

set1.add("apple")

print(set1)

set1.update(set2)
print(set1)

set1.update(list1)

print(set1)

set1.remove("banana")
set1.discard("forward")

print(set1)

x = set1.pop()
print(x)



set3 = {"1" , "2" , "3"}
set4 = {"a" , "b" , "c"}

set5 = set3.union(set4)

print(set5)