'''
factorial(1) =  1 
factorial(2) =  2 X 1 
factorial(3) =  3 X 2 X 1 
factorial(4) =  4 X 3 X 2 X 1 
factorial(5) =  5 X 4 X 3 X 2 X 1 

factorial (n) = factorial (n) X factorial (n-1)
'''
# n = int(input("Enter A Number: "))
# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n * factorial (n-1)

# print(f"The Factorial of This Number Is: {factorial(n)}")


# n = int(input("Enter A Number: "))
# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(f"The facatorial of the number is : {factorial(n)}")

n = int(input("Enter A Number: "))
def factorial(n):
    if n==1 or n==0:
        return 1
    
    return n * factorial(n-1)

print(f"The factorila of this number is : {factorial(n)}")