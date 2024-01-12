""" Please write a program which asks the user to type in a string. The program then prints out all the substrings which begin with the first character, from the shortest to the longest.  """
word = input("Word: ")
limit = len(word)
for i in range(0,limit,1):
    for j in range(0,i,1):
        print(word[j],end="")
    print(word[i])