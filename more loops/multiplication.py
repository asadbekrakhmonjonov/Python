""" lease write a program which asks the user for a positive integer number. The program then prints out a list of multiplication operations until both operands reach the number given by the user. """
number = int(input("Please type in a number: "))
for i in range(1, number + 1):
    for j in range(1, number + 1):
        print(f"{i} x {j} = {i * j}")
