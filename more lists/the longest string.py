def longest(strings: list):
    n = 0
    longest = strings[n]
    for words in strings:
        if len(words) > len(longest):
            longest = words
    print(longest)
if __name__ == "__main__":
    longest(["hi", "hiya", "hello", "howdydoody", "hi there"])