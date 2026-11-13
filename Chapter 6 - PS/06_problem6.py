# marks = int(input("Enter Your Marks:- "))

# if(marks>=90 and marks<=100):
#     grade = "EX"  
# elif(marks>=80 and marks<=89):
#     grade = "A" 
# elif(marks>=70 and marks<=79):
#     grade = "B"
# elif(marks>=60 and marks<=69):
#     grade = "C"
# elif(marks>=50 and marks<=59):
#     grade = "D" 
# else:
#     grade = "F" 

# grade =  ("Your Grade Is:-",grade)

marks = int(input("Enter Your Marks:- "))

if(marks<=100 and marks>=90):
    grade = "Ex"
elif(marks>=80 and marks<90):
    grade = "A"
elif(marks>=70 and marks<80):
    grade = "B"
elif(marks>=60 and marks<70):
    grade = "C"
elif(marks>=50 and marks<60):
    grade = "D"
elif(marks<50):
    grade = "F"

print("Your Grade Is:- ",grade)