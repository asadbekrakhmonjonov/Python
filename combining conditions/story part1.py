""" Please write a program which keeps asking the user for words. If the user types in end, the program should print out the story the words formed, and finish.
 Part 2
Change the program so that the loop ends also if the user types in the same word twice."""
words = []
condition = "end"
word = input("Please type in a word: ")
words.append(word)

while word.lower() != condition:
    word = input("Please type in a word: ")
    if word.lower() in words[-1:]:
        break
    words.append(word)
length = len(words)
if word.lower() == "end":
    for k in range(length - 1):
        print(words[k],end=" ")
else:
    length2 = len(words)
    for j in range(length2):
        print(words[j],end =" ")


