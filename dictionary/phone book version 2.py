def phone_book():
    phonebook = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))
        if command == 3:
            break
        elif command == 2:
            name = input("name: ")
            phone = int(input("phone number: "))
            if name in phonebook:
                phonebook[name].append(phone)
            else:
                phonebook[name] = [phone]
        elif command == 1:
            name = input("name: ")
            if name in phonebook:
                for key, value in phonebook.items():
                    print()
                    for word in value:
                        print(word)
            else:
                print(f"No entry found for {name}")

phone_book()
