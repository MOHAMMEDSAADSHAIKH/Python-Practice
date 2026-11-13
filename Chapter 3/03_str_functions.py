# name = "Saad Shaikh"
# length = len(name)#This len function prints the length of the string or the integer value with which includes everything like the decimal points and also the spacing between the words
# print(length)

# print(name.endswith('ad'))#This and print(name.startswith("Sa")) returns a boolean value and the string that is written inside it is case sensitive
# print(name.startswith("Sa"))#Checks whether the string value starts with 'Sa' or not this is case sensitive means "Sa" and "sa" is different
# print(name.startswith("sa"))
# print(name.capitalize())#This only capitalizes the first alphabet of the string value and not the entire name or string value
# print(name.find ("d"))#This tells the array index value where the first 'd' later is introduced in the string like in the name "Saad Shaikh" the first time the letter 'd' is introduced is in the array index value of 3
# print(name.replace("Shaikh","Khan"))#The format is that it replaces the old word with the new word and first the old word is written in single or double quotes and then the new word is written just after it 
# print(name.replace("Shaikh","Alam"))


# name1 = "Saad is a very good good boy"
# name_replaced = name1.replace("good","GOOD")
# print(name1)
# print(name_replaced)
# print(name1.replace("good","bad"))#The replace function replaces everything eventhough the old word is occuring again and again in the sentence with the new word with the same amount of time

name = "Mohammed Saad Shaikh"
length = len(name)
print(length)

print(name.startswith("Mo"))
print(name.startswith("mo"))
print(name.endswith("kh"))
print(name.endswith("Kh"))
print(name.capitalize())
print(name.find("o"))
print(name.replace("Mohammed",""))
print(name.replace("Shaikh","Maham"))
length1 = len(name.replace("Shaikh","Maham"))
print(length1)

