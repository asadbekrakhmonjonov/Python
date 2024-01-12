def add_items():
    n = 1
    list = []
    number = int(input("How many items: "))
    while n <= number:
        item = int(input("Item" + str(n) + ": "))
        n += 1
        list.append(item)
    print(list)
add_items()