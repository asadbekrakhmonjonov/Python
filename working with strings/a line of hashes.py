""" Please write a program which prints out a line of hash characters, the width of which is chosen by the user. """
width = int(input("Width: "))
height = int(input("Height: "))
for i in range(height):
    for j in range(width):
        print("#",end="")
    print()