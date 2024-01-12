def length_of_longest(list):
    n = 0
    longest = len(list[n])
    for words in list:
        if len(words) > longest:
            longest = len(words)
    print(longest)
    return
if __name__=="__main__":
    length_of_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"])