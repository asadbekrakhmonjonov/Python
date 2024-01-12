def print_first_letters(sentence):
    words = sentence.split()
    for word in words:
        print(word[0])

# Get input from the user
user_sentence = input("Please type in a sentence: ")

# Print the first letter of each word on a separate line
print_first_letters(user_sentence)
