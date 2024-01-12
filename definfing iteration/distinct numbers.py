def distinct_numbers(lst):
    distinct_set = set()
    for number in lst:
        distinct_set.add(number)
    return distinct_set

if __name__ == "__main__":
    result = distinct_numbers([3, 2, 1, 1, 3, 3, 1])
    print(result)
