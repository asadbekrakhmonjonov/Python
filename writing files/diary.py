def diary_reader():
    while True:
        with open("diary.txt", "a+") as my_file:
            print("1 - add an entry, 2 - read entries, 3 - quit")
            function = int(input("Function: "))

            if function == 3:
                print("Quitting...")
                break
            elif function == 1:
                entry = input("Diary entry: ")
                my_file.write(entry + "\n")
                print("Diary entry saved.")
            elif function == 2:
                my_file.seek(0)
                entries = my_file.read()
                if not entries:
                    print("No entries found.")
                else:
                    print("Entries:")
                    print(entries)
            else:
                print("Invalid function. Please enter 1, 2, or 3.")

diary_reader()
