# n1 = int(input("Enter Number 1: "))
# n2 = int(input("Enter Number 2: "))
# n3 = int(input("Enter Number 3: "))
# def great(n1,n2,n3):
#     if (n1>n2 and n1>n3):
#         return n1
#     elif (n2>n1 and n2>n3):
#         return n2
#     elif (n3>n1 and n3>n2):
#         return n3
# print(f"The greatest of the three number is : {great(n1,n2,n3)}")

n1 = int(input("enter number 1: "))
n2 = int(input("enter number 2: "))
n3 = int(input("enter number 3: "))

def greatest(n1,n2,n3):
    if (n1>n2 and n1>n3):
        return n1
    elif (n2>n1 and n2>n3):
        return n2
    elif (n3>n1 and n3>n2):
        return n3
print(f"The greatest of the 3 numbers is : {greatest(n1,n2,n3)}")

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")



def great(n1,n2,n3):
    if (n1>n2 and n1>n3):
        return n1
    elif (n2>n1 and n2>n3):
        return n2
    elif(n3>n1 and n3>n2):
        return n3
n1 = 123
n2 = 41341
n3 = 139393123
print(f"The greates of the three numbers is : {great(n1,n2,n3)}")