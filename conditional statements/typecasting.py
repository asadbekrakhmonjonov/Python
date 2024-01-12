""" # Write your solution here
word = input("Please type in a word: ")
length = len(word)
if length > 1:
    print(f"There are {length} letters in the word {word}",end="\n")
    print("Thank you!")
else:
    print("Thank you!") """
# Write your solution here
number = float(input("Please type in a number: "))
print(f"Integer part:{int(number)}")
print(f"Decimal part: {number - int(number)}")