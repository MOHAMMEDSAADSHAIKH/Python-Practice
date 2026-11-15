# n = int(input("Enter A Number: "))
# for i in range(1,11):
#     print(f"{n} X {11-i} = {n * (11-i)}")

print("Table In Correct Order!")
n = int(input("Enter A Number: "))
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")
print("Table In Reverse Order!")
n = int(input("Enter A Number: "))
for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")