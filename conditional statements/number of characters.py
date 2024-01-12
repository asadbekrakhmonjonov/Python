""" he function len can be used to find out the length of a string, among other things. The function returns the number of characters in a string.

Some examples of how this works:word = "abcd"
print(len(word))

print(len("hi there"))

word2 = "howdydoody"
length = len(word2)
print(length)

empty_string = ""
length = len(empty_string)
print(length)"""

# Write your solution here
word = input("Please type in a word: ")
length = len(word)
if length > 1:
    print(f"There are {length} letters in the word {word}",end="\n")
    print("Thank you!")
else:
    print("Thank you!")
