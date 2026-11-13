# p1 = "make a lot of money"
# p2 = "buy now"
# p3 = "click this"
# p4 = "subscribe this"

# message = input("Enter Your Comment:- ")

# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("This Is A Spam")

# else:
#     print("This Is Not A Spam")


# spam_phrases = [
#     "make a lot of money",
#     "buy now",
#     "click this",
#     "subscribe this"
# ]

# # Get user input and convert it to lowercase for accurate, case-insensitive matching
# message = input("Enter Your Comment:- ").lower()

# # any() iterates through the list and triggers if at least one phrase is found in the message
# if any(phrase in message for phrase in spam_phrases):
#     print("This Is A Spam")
# else:
#     print("This Is Not A Spam")

p1 = "subscribe this"
p2 = "click here"
p3 = "buy now"
p4 = "offer"

message = input('enter your comment here:- ')

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This Is A Spam")

else:
    print("This Is Not A Spam")