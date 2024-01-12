""" Please write a program which asks the user for an integer number. The program should then print out the magnitude of the number according to the following examples.

Please type in a number: 950
This number is smaller than 1000
Thank you!

 Please type in a number: 59
This number is smaller than 1000
This number is smaller than 100
Thank you!

Please type in a number: 2
This number is smaller than 1000
This number is smaller than 100
This number is smaller than 10
Thank you!

Please type in a number: 1123
Thank you! """

# Write your solution here
def compare():
    number = int(input("Please type in a number: \t"))
    f = ["\nThis number is smaller than 1000",
         "\nThank you!\n"]
    if 100 <= number < 1000:
        for i in f:
            print(i)
    if 10 <= number < 100:
        f.insert(1,"\nThis number is smaller than 100")
        for i in f:
            print(i)
    if 1 <= number < 10:
        f.insert(1,"\nThis number is less than 100")
        f.insert(2,"\nThis number is smaller than 10")
        for i in f:
            print(i)
    if number >= 1000:
        print(f[1])

compare()