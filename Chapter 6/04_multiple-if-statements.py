age = int(input("Enter Your Age:- "))

#start of the first independent if statement
if(age>18):
    print("You Are An \"Adult\"")

else:
    print("You Are Not An \"Adult\"")

#end of if - else ladder no: 1 

#start of if - elif -else laddder
if(age>18):
    print("You are eligible to drive")

elif(age == 0):
    print("Age can't be 0")

elif(age < 0):
    print("Age can't be negative")

else:
    print("You Are Not Eligible To Drive")

#End Of if - elif - else ladder
print("End Of Program")