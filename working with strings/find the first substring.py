word = input("Please type in a string: ")
character = input("Please type in a character: ")
i = word.find(character)
j = i + 3
if character in word and j <= len(word):
    print(word[i : j])
else:
    print()


