# n = int(input("Enter The Value Of A Natural Number: "))
# def sum(n):
#     if n == 1:
#         return 1
#     return sum(n-1) + n
# print(sum(10))


# def sum(n):
#     if n == 1:
#         return 1
#     return sum(n-1) + n
# print(sum(23))

'''
sum (1) = 1
sum (2) = 1 + 2
sum (3) = 1 + 2 + 3
sum (4) = 1 + 2 + 3 + 4
sum (5) = 1 + 2 + 3 + 4 + 5
sum (6) = 1 + 2 + 3 + 4 + 5 + 6
'''
def sum(n):
    if n ==1:
        return 1
    return sum(n-1) + n
print(sum(8))