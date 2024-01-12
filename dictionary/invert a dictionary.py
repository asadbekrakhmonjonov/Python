def invert(dictionary:dict):
    inverted = {}
    for key,value in dictionary.items():
        inverted[value] = inverted.get(value,[])+[key]
    print(inverted)
if __name__ == '__main__':
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)