def meaningful_words(my_list):
    n = 0
    shortest = my_list[n]
    for words in my_list:
        if len(words) < len(shortest):
            shortest = words
    print(shortest)
    return
if __name__=="__main__":
    meaningful_words(["first", "second", "fourth", "eleventh"])
    meaningful_words(["adele", "mark", "dorothy", "tim", "hedy", "richard"])