# def rem(l,word):
#     n = []
#     for item in l:
#         if not (item == word):
#             n.append(item.strip(word))
#     return n

# l = ["Harry","Rohan","Saad","an"]
# print(rem(l,"an"))


# def rem(l,word):
#     n = []
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n
# l = ["Mohammed Saad Shaikh","Moinuddin","Anas","Asif"]
# print(rem(l,"an"))

def rem(l,word):
    n = []
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
l = ["Saad","Mohammed","Moin","Arif","an"]
print(rem(l,"an"))

# def rem(l,word):
#     n = []
#     for item in l:
#         if not(item==word):
#             n.append(item.strip(word))
#     return n
# l = ["Saad","Ron","Corn"]
# print(rem(l,"an"))

# def rem(l,word):
#     n = []
#     for item in l:
#         if not(item==word):
#             n.append(item.strip(word))
#     return n
# l = ["animal","minimal","calories"]
# print(rem(l,"al"))

# def rem(l,word):
#     n = []
#     for item in l:
#         if not(item==word):
#             n.append(item.strip(word))
#     return n
# l = ["saad","saadu"]
# print(rem(l,"sa"))

def rem(l,word):
    n = []
    for item in l:
        if not (item==word):
            n.append(item.strip(word))
    return n
l = ["Saad","Saadu","Daadu","Daadi"]
print(rem(l,"Sa"))