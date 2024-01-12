def list_twice():
    list = []
    number = int(input("New item: "))
    list_in_order = sorted(list)
    while True:
        list_in_order = sorted(list)
        list.append(number)
        print("\nThe list now:",list)
        print("\nThe list in order:",sorted(list))
        number = int(input("\nNew item: "))
        if number == 0:
            break
    print("\nThe list now:",list,end="\n")
    print("\nThe list in order:",sorted(list),end="\n")
list_twice()

