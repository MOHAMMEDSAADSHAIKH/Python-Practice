# # n = int(input("Enter A Number: "))#enter n = 3
# # for i in range(1,n+1):
# #     if i == 1 or i == n:
# #         print("*" * n,end="")
# #     else:
# #         print("*",end="")
# #         print(" " * (n-2),end="")
# #         print("*",end="")
# #     print("")

# '''
# ***
# * *
# ***
# '''
# n = int(input("Enter A Number: ")) #n=3
# for i in range(1,n+1):
#     if i == 1:
#         print(" " * (n-i),end="")
#         print("*" * i,end="")
#     elif (i == 2 or n):
#         print(" " * (n-1),end="")
#         print("*" * (2*i-1),end="")
#     elif(n+1):
#         print("*" * (2*i+1),end="")
# print("")


# n = 5
#     *
#    ***
#   *****
#  *******
# *********
#

#     *
#    ***
#   *****
#   *
#  ***
# *****

print('a')
print('b')
print('c',end = "")#the end="" helps to prevent new line from forming in python
print('d',end = "")