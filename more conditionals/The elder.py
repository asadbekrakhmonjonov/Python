""" Please write a program which asks for the names and ages of two persons. The program should then print out the name of the elder.

Some examples of expected behaviour:

Person 1:
Name: Alan
Age: 26
Person 2:
Name: Ada
Age: 27
The elder is Ada """

# Write your solution here
print("Person1:")
name1 = input("Name:")
age1 = int(input("Age:"))
print("Person2:")
name2 = input("Name:")
age2 = int(input("Age:"))
if age1 > age2:
    print(f"The elder is {name1}")
elif age2 > age1:
    print(f"The elder one is {name2}")
else:
    print(f"{name1} and {name2} are the same age")