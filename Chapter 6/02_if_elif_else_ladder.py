a = int(input("Enter your Age:- "))

#If - Elif - Else ladder

if(a>=18 and a<=100):
    print("You Are Above The Age Of Consent")
    print("Good For You")

elif(a>100):
    print("What the funge!")

elif(a<0):
    print("You are entering a negative age which is not quite valid")

elif(a == 0):
    print("Age can't be 0")

else:
    print("You are not above the age of consent")
    print("Please bring your parents with you")