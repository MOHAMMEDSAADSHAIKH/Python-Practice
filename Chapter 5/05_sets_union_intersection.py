# s1 = {1,2,3,4,5,11,12}
# s2 = {9,10,11,12,13}

# # print (s1.union(s2))#adds both the sets
# # print(s1.intersection(s2))#gives the common terms / values of both the sets 
# print(s1.pop())
# # print(s2.remove("10))


s = {1,2,3,6,7,8,4,5}
s_ = {6,7,8,9,10}

print(s)
print(s_)
print(s.union(s_))#adds both the sets together not like addition but more like concatenation but in this the repeted values are not taken
print(s.intersection(s_))#gives the common terms if no common terms are found then returns set()
print(s.pop())#removes a random value from the set 's' and displays the poped value in the terminal/output screen
# print(s_.remove('6'))#removes the value that you put 