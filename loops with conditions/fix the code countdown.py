""" This exercise is similar to the countdown exercise in the last section, but please don't use a while True loop this time round! """
# Fix the program
print("Are you ready?")
number = int(input("Please type in a number: "))
for i in range(number,0,-1):
    print(i)
print("Now!")