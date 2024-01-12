def all_the_longest(my_list):
    n = 0
    longest = my_list[n]
    equal = []

    for words in my_list:
        if len(words) > len(longest):
            longest = words
            equal = [longest]
        elif len(words) == len(longest):
            equal.append(words)

    return equal

if __name__ == "__main__":
    result = all_the_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"])
    print(result)  # ['dorothy', 'richard']
