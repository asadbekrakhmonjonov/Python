""" Please write a program which asks the user for a string. The program then prints out the input string in reversed order, from end to beginning. Each character should be on a separate line. """
string = input("Please type in a string: ")
string2 = string[::-1]
index = 0
while index < len(string2):
    print(string2[index])
    index += 1