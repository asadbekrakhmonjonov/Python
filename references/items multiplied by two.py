def double_items(numbers:list):
    doubled_list =[]
    for i in numbers:
        i *= 2
        doubled_list.append(i)
    return doubled_list
if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)