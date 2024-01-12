def addition_or_removal():
    my_list = []
    print("The list now is",my_list)
    while True:
        action = input("(a)adding\t (r)remove\t (e)exit\t: ")
        if action == "a":
            my_list.append(len(my_list)+1)
        elif action == "r":
            if my_list:
                my_list.pop()
        elif action == "e":
            print("Bye!")
            break
        else:
            print("Invalid user input")
            continue
        print("This is the list now",my_list)
addition_or_removal()





addition_or_removal()