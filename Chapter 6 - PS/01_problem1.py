#print the greatest of the 4 numbers entered by the user

# a1 = int(input("Enter Number 1: "))
# a2 = int(input("Enter Number 2: "))
# a3 = int(input("Enter Number 3: "))
# a4 = int(input("Enter Number 4: "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("The greatest number is a1: ",a1)

# elif(a2>a1 and a2>a3 and a2>a4):
#     print("The greatest number is a2: ",a2)

# elif(a3>a1 and a3>a2 and a3>a4):
#     print("The greatest number is a3: ",a3)

# elif(a4>a1 and a4>a2 and a4>a3):
#     print("The greatest number is a4: ",a4)

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))

if(a>b and a>c and a>d):
    print("Number 1 is the greatest: ",a)
if(b>a and b>c and b>d):
    print("Number 2 is the greatest: ",b)
if(c>a and c>b and c>d):
    print("Number 3 is the greatest: ",c)
if(d>a and d>b and d>c):
    print("Number 4 is the greatest: ",d)