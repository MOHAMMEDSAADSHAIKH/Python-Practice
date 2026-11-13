# marks = {
#     "Saad" : 100,
#     "Affan" : 90,
#     "Arsalan" : 83,
#     "Abu-Zaid" : 60
# }

# print(marks)

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Saad" : 99, "Rahul" : 20})
# print(marks)


# grades = {
#     "Saad" : "A",
#     "Saif" : "B",
#     "Arsalan" : "C",
#     "Ashraf" : "A+"
# }

# print(grades)

# print(grades.items())
# print(grades.keys())
# print(grades.values())
# grades.update({"Saad" : "A+", "Affan" : "A"})
# print(grades)

# surnames = {
#     "Saad" : "Shaikh",
#     "Arsalan" : "Ansari",
#     "Ibrahim" : "Haji",
#     "Ibrahim2" : "Sassa"
# }

# # print(surnames)
# # print(surnames.items())
# # print(surnames.keys())
# # print(surnames.values())
# # surnames.update({"Ibrahim2" : "Khan", "Ashraf" : "Shaikh"})
# # print(surnames)


# print(surnames.get("Ibrahim"))
# print(surnames["Ibrahim"])
# print(surnames.get("Saad"))#prints none if the value is not present in the key value pair 
# print(surnames["Saad"])#gives a KeyError if the statement is not present

# bike = {
#     "Saad" : "Chetak",
#     "Affan" : "Burgman",
#     "Fahim" : "None",
#     "Ashraf" : "Passion"
# }

# print(bike)
# print(bike.items())
# print(bike.keys())
# print(bike.values())
# bike.update({"Saad" : "Ola", "Affan" : "Aprilla","Fahim" : "Hunter 650"})
# print(bike)
# print(bike.items())
# print(bike.get("Saad"))


# house = {
#     "Saad" : "Apartment",
#     "Arsalan" : "Independent - House",
#     "Ashraf" : "Independent - House",
#     "Moiz" : "Apartment" 
# }

# print(house)

# print(house.get("Saad"))

# print(house["Saad"])

# print(house.items())

# print(house.keys())

# print(house.values())


# house.update({"Saad" : "Indepent-House"})
# print(house)



grades = {
    "Saad" : "A+",
    "Ibrahim" : "A",
    "Ashraf" : "O",
    "Moiz" : "B+"
}

print(grades)

print(grades.items())

print(grades.keys())

print(grades.values())

print(grades.get("Moiz"))

print(grades["Saad"])

grades.update({"Saad" : "O"})

print(grades["Saad"])

print(type(grades))