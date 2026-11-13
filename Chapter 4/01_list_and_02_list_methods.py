# name = ["Rohan","Rahul","Saad","Javed",12321231,1313123139.123123,True,False]
# # print(name[0:8])
# # name[0] = "Raj"
# # print(name[0])#lists are mutable which means that the value can be changed and the changed value is stored in the original list elements unlike string which is immutable i.e. for performing and printing a new function in string it creates a different string and then we have to print the new string to get the desired result and the original strig remains intact
# name[2] = "Mohammed Saad Shaikh"
# print(name[2])

# l1 = [123,12,41,9,10,1,4]
# print(l1)
# l1.sort()
# print(l1)
# l1.reverse()
# print(l1)
# l1.insert(1,1)
# print(l1)


fruits = ["Apple","Banana","Pineapple","Guava"]
print(fruits)
fruits.append("Green - Apple")
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits.pop(2)#you are just giving the index number of the item you want to get rid of without actually righting the list number or name you want to get rid of 
print(fruits)
fruits.remove("Apple")#you have to write the thing you want to get rd of in the list items 
print(fruits)