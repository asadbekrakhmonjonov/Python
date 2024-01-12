""" Please change the program from the previous exercise so that the user gets to input also the base which is multiplied (in the previous program the base was always 2). """
# Write your solution here
ask = int(input("Upper limit: "))
n = int(input("Base:"))
number = 1
while number <= ask:
    print(number)
    number = n * number
