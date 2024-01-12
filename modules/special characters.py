from string import ascii_letters, punctuation, whitespace

def separate_characters(my_string: str):
    letters = ''.join(char for char in my_string if char in ascii_letters)
    punctuation_chars = ''.join(char for char in my_string if char in punctuation)
    whitespace_chars = ''.join(char for char in my_string if char in whitespace)
    return letters, punctuation_chars, whitespace_chars

if __name__ == '__main__':
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
    