def first_word(string):
    string = string.split()
    return string[0]
def second_word(string):
    string = string.split()
    return string[1]
def last_word(string):
    string = string.split()
    return string[-1]
sentence = "it was a dark and stormy python"
print(first_word(sentence))
print(second_word(sentence))
print(last_word(sentence))