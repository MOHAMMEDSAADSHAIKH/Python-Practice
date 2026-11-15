#for n = 3
# n = int(input("Enter Any Number: "))
# for i in range(1,n+1):
#     print(" " * (n-i),end = "")
#     print("*" * (2*i-1),end = "")
#     print("")
print("when i = 1")
n = int(input("Enter Any Number: "))
for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("*" * (2*i-1),end="")
    print("")

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("when i = 0")
n = int(input("Enter Any Number: "))
for i in range(n):
    print(" " * (n-i-1),end="")
    print("*" * (2*i+1),end="")
    print(" ")