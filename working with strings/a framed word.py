""" Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame. """
import math
string = input("Word: ")
padding = 30 - 2 - len(string)
if padding % 2 == 0:
    left_padding = right_padding = padding // 2
else:
    left_padding = padding // 2
    right_padding = padding // 2 + 1
width = "*"*30
print(width)
print("*" + " "*right_padding + string + " " *left_padding + "*")
print(width)
