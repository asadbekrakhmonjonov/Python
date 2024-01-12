def palindrome():
    user = input("Please type in a palidrome: ")
    user1 = reversed(user)
    for letter in user:
        letter = letter
    for word in user1:
        word = word
    while True:
        if letter != word:
            for letter in user:
                letter = letter
            for word in user1:
                word = word
            print("that wasn't a palindrome")
            user = input("Please type in a palidrome: ")
        else:
            print(user, "is a palindrome")
        return
if __name__=="__main__":
    palindrome()
