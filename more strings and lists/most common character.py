def most_common(first_string):
    n = 0
    common = first_string.count(first_string[n])
    for words in first_string:
        result = first_string.count(words)
    print(first_string[result])

if __name__=="__main__":
    most_common("abcdbde")
    most_common("exemplaryelementary")

