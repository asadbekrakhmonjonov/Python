""" Please write a program which asks the user for two words. The program should then print out whichever of the two comes alphabetically last.

You can assume all words will be typed in lowercase entirely.

Some examples of expected behaviour:

Sample output
Please type in the 1st word: car
Please type in the 2nd word: scooter
scooter comes alphabetically last. """
# Write your solution here
word1 = input("Please type in the 1st word:").lower()
word2 = input("Please type in the 2nd word:").lower()
if word1 > word2:
    print(f"{word1} comes alphabetically first")
elif word2 > word1:
    print(f"{word2} comes alphabetically last")
else:
    print("You gave the same word twice.")