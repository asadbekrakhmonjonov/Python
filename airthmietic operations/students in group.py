""" Please write a program which asks for the number of students on a course and the desired group size. The program will then print out the number of groups formed from the students on the course. If the division is not even, one of the groups may have fewer members than specified.
 """

# Write your solution here
import math
students = int(input("How many students on the course?"))
groups = int(input("Desired group size?"))
res = students / groups
print("Number of groups formed:",math.ceil(res))