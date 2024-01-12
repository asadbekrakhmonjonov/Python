def everything_reversed(my_list):
    new_list = []
    for words in my_list:
        words = words[::-1]
        new_list.append(words)
    print(new_list[::-1])
if __name__=="__main__":
    everything_reversed(["Hi", "there", "example", "one more"])