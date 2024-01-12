def change_the_value():
    list = [1,2,3,4,5]
    index = int(input("Index: "))
    value = int(input("Value: "))
    while index != -1:
        list[index] = value
        print(list)
        index = int(input("Index: "))
        value = int(input("Value: "))
    else:
        return
change_the_value()