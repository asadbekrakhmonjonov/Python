""" This program calculates the end of year bonus a customer receives on their loyalty card. The bonus is calculated with the following formula:

If there are less than a hundred points on the card, the bonus is 10 %
In any other case the bonus is 15 %
The program should work like this: """

# Fix the program
points = int(input("How many points are on your card? "))
bonus1 = points + (points * 0.1)
bonus2 = points + (points * 0.15)
if points < 100:
    print("Your bonus is 10 %")
    print(f"You now have {bonus1} points")
else:
     print("Your bonus is 15 %")
     print(f"You now have {bonus2} points")
