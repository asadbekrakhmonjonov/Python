""" Please write a program which asks the user for a string. The program then prints out a message based on whether the second character and the second to last character are the same or not. """
string = input("Please type in a string: ")
if string[1] == string[-2]:
    print(f"The second and the second to last characters are {string[1]}")
else:
    print("The second and the second to last characters are different")