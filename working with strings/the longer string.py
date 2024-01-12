"""  Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters. If the strings are of equal length, the program should print out "The strings are equally long".   """
# Write your solution here
string1 = input("Please type in a string 1: ")
string2 = input("Please type in a string 2: ")
if len(string1) > len(string2):
    print(f"{string1} is longer")
elif len(string2) > len(string1):
    print(f"{string2} is longer")
elif len(string1) == len(string2):
    print("The strings are equally long")