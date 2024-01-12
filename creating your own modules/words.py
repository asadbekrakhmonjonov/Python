def first_word(my_string:str):
    parts = my_string.split(" ")
    return parts[0]
def last_word(my_string:str):
    parts = my_string.split(" ")
    return parts[-1]
def number_of_words(my_string:str):
    parts = my_string.split(" ")
    return len(parts)
if __name__ == "__main__":
    my_string = "Sheila sells seashells by the seashore"

    print(first_word(my_string))
    print(last_word(my_string))
    print(number_of_words(my_string))
