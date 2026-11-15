#  n = int(input("Enter Any Number Of Your Choice: "))
# for i in range(1,11):
#     print(f"{n} X {i} = {n * i}")
# print("The below one is done by using the while loop!")
# y = int(input("Enter Any Number: "))
# i = 1
# while (i<=10):
#     print(f"{y} X {i} = {y * i}")
#     i=i+1

# print ("This below one is done by using for loop!")

# z = int(input("Enter Number: "))
# for i in range (1,11):
#     print(f"{z} X {i} = {z * i}")
# print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
# name = ["Saad","Rohan","Rahul","Sachin","Sohail"]
# for i in name:
#     if i.startswith("S"):
#         print(f"Hello {i}")
print("Printing Table Using While Loop")
n = int(input("Enter Any Number: "))
i = 1
while(i<=10):
    print(f"{n} X {i} = {n * i}")
    i+=1

print("Printing Table Using For Loop")
n = int(input("Enter Any Number: "))
i = 1
for i in range(1,11):
    print(f"{n} X {i} = {n * i}")