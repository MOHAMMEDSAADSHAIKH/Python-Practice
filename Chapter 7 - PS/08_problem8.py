#Just removed print(" " * (n*i)) from the first row of the print statement
n = int(input("Enter A Number: "))
for i in range(1,n+1):
    print("*" * (2*i-1),end = "")
    print("")

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#Just added print ("*" * (i),end="") instead of ("*" * (2*i-1),end="")
n = int(input("Enter A Number: "))
for i in range(1,n+1):
    print("*" * (i),end="")
    print("")