#for n = 3
# n = int(input("Enter A Number: "))
# for i in range(1,n+1):
#     print("*" * (n),end="")
#     print(" " * (2*i-1),end="")
#     print("*" * (n),end="")
#     print(" " * (2*i-1),end="")
#     print(("*") * (n),end="")
#     print("")

# n = int(input("Enter A Number: "))

# for i in range(1, n + 1):
#     print("*" * n, end="")          # First block of stars (always n)
#     print(" " * i, end="")          # First block of spaces (increases with i)
#     print("*" * (n - i), end="")    # Middle block of stars (decreases with i)
#     print(" " * i, end="")          # Second block of spaces (increases with i)
#     print("*" * n)                  # Last block of stars (always n)


# n = int(input("Enter A Number: "))
# for i in range(1,n+1):
#     print("*" * n,end="")
#     print("")
#     print(("*" * (n-2*i))*( "*" * (n-2*i)),end="")
#     print("")
#     print("*" * n,end="")
#     print("")
# n = int(input("Enter A Number: "))

# for i in range(n):
#     # If it is the first row (i=0) or the last row (i=n-1)
#     if i == 0 or i == n - 1:
#         # Print a solid line of 'n' stars
#         print("*" * n)
#     else:
#         # Print a single star, followed by (n-2) spaces, followed by a final star
#         print("*" + " " * (n - 2) + "*")

# n = int(input("Enter A Number: "))
# for i in range(1,n+1):
#     if (i == 1 or i == n):
#         print("*" * n,end="")
#     else:
#         print("*" ,end="")
#         print(" " * (n-2),end="")
#         print("*" ,end="")
#     print("")

n = int(input("Enter A Number: "))
for i in range(1,n+1):
    if i == 1 or i == n:
        print("*" * n,end="")
    else:
        print("*",end="")
        print(" " * (n-2),end="")
        print("*",end="")
    print("")