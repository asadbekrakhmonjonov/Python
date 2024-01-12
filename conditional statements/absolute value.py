""" Please write a program which asks the user for an integer number. If the number is less than zero, the program should print out the number multiplied by -1. Otherwise the program prints out the number as is. Please have a look at the examples of expected behaviour below.
 Please type in a number: -7
The absolute value of this number is 7
Please type in a number: 1
The absolute value of this number is 1 """

#Write your solution here
number = int(input("Please type in a number:"))
if number < 0:
    print(f"The absolute value of this number is {number * (-1)}")
else:
    print(f"The absolute value of this number is {number}")

