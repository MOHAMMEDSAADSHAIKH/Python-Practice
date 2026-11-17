# def rem(l,word):
#     n = []
#     for item in l:
#         if not (item == word):
#             n.append(item.strip(word))
#     return n

# l = ["Harry","Rohan","Saad","an"]
# print(rem(l,"an"))


def rem(l,word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
l = ["Mohammed Saad Shaikh","Moinuddin","Anas","Asif"]
print(rem(l,"an"))