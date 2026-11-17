#for n = 3
# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)

# pattern(10)
# def pattern(n):
#     if n == 0:
#         return
#     print("*" * n)
#     pattern(n-1) 
# pattern(3)


# def pattern(n):
#     if n==0:
#         return
#     else:
#         print("*" * n)
#         pattern(n-1)
# pattern(5)


def pattern(n):
    if  n == 0:
        return
    print("*" * n)
    pattern(n-1)

pattern(6)