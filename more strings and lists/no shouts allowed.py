def no_shouting(my_list):
    for words in my_list:
        if words.isupper():
            result = my_list.remove(words)
    return my_list
if __name__=="__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
