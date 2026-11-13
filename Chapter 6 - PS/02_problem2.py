# s1 = int(input("Enter The Marks Of Biology:- "))
# s2 = int(input("Enter The Marks Of Physics:- "))
# s3 = int(input("Enter The Marks Of Chemsitry:- "))

# total_percentage = (((s1+s2+s3)/300)*100)

# if(total_percentage>=40 and s1>=33 and s2>=33 and s3>=33):
#     print(f"You Passed The Exam And Got {total_percentage}%")

# else:
#     print(f"You have failed the exam and got {total_percentage}%")

# # if((((s1+s2+s3)/300)*(40/100)) and ((s1/100)*33) and ((s2/100)*33) and ((s3/100)*33)):
# #     print("You Have Passed The Exam!")

# # else:
# #     print("You Have Failed The Exam!")

# marks1 = int(input("Enter Marks 1: "))
# marks2 = int(input("Enter Marks 2: "))
# marks3 = int(input("Enter Marks 3: "))

# total_percentage = (((marks1+marks2+marks3)/300)*100)



# if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print(f"You have passed the exam by {total_percentage:.2f}% and the percentage you got in subject 1 is {marks1} % and in subject 2 is {marks2}% and in subject 3 is {marks3}% ")

# else:
#     print(f"You didn't pass the exam your overall percentage was {total_percentage:.2f}% and in sub1 was {marks1:.2f}% and in sub2 was {marks2:.2f}% and in sub3 was {marks3:.2f}%")


m1 = int(input("Enter The Marks For Maths:- "))
m2 = int(input("Enter The Marks For Science:- "))
m3 = int(input("Enter The Marks For SST:- "))

total_percentage = (((m1 + m2 + m3)/300)*100)

if(total_percentage>=40 and m1>=33 and m2>=33 and m3>=33):
    print(f"You have passed the exam by {total_percentage:.2f}%")
else:
    print(f"You have failed the exam by {total_percentage:.2f}%")