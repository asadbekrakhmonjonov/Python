def remove_smallest(numbers: list):
    n = 0
    shortest = numbers[n]
    for items in numbers:
        if items < shortest:
            shortest = items
    numbers = numbers.remove(shortest)
    return numbers
if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)
