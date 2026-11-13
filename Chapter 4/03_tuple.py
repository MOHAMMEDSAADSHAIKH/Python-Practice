# #Tuple is always represented in "()" breaces
# a = (1,123,412,"Saad","Rahul","Rohan","Shivam","Saad","Saad")
# print(a)
# print(type(a))
# count = a.count("Saad") #provides us with the count of how many times the particular word or numebr is occuring in the tuple
# print(count)
# index = a.index("Saad") #gives the index value of the element that we want 
# print(index)

# t1 = (1,2,3,4,5)
# t2 = (6,7,8,9,10)
# concatenation = t1 + t2 
# print(concatenation)#this concatenates i.e. joins one tuple with the another tuple 

# T1 = (5,10,15,20,25,30)
# repetation = T1 * '\n' 5
# print(repetation)

# T1 = (5, 10, 15, 20, 25, 30)

# repetition = '\n'.join([str(T1)] * 5)
# print(repetition)

a = ("Saad","Saad","Rohan","Rahul")
b = ("Raju","Taju","Jiju")
print(a)
# a.sort()
# print(a)
i = a.index("Rohan")#Shows the indexing value of Rohan in the tuple  
print(i)
y = a.count("Saad")#Counts how many of the elements are there named "Saad" in the tuple
print(y)
c = a + b
print(c)
d = a * 2
print(d)