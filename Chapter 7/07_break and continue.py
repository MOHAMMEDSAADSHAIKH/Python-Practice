for i in range(100):
    if i == 50:
        break #this exists the loop when the value reaches 50 without continuing further
    print(i)

print("XXXXXXXXXXXXXXXXXXXXXXX")

for i in range(0,100):
    if i == 50: #this continue statement helps us to skip the particular iteration and move on to the enxt one without exiting the loop
        continue
    print(i)

print("XXXXXXXXXXXXXXXXXXXXXXX")

for i in range(10):
    if i == 5:
        break
    print(i)


print("XXXXXXXXXXXXXXXXXXXXXXX")

for i in range(10):
    if i == 5:
        continue
    print(i)

