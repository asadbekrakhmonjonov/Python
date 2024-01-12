""" Please make an extended version of the previous program, which prints out all the substrings which are at least three characters long, and which begin with the character specified by the user. You may assume the input string is at least three characters long.

 """
word = input("Please type in a word: ")
start_char = input("Please type in a character: ")

index = 0
while index < len(word):
    if word[index] == start_char:
        substring = word[index:index+3]
        if len(substring) == 3:
            print(substring)
        index += 1
    else:
        index += 1