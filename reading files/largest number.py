with open("numbers.txt") as new_file:
    new_list = []
    for number in new_file:
        number = number.replace("\n", "")
        new_list.append(int(number)) 

    largest = new_list[0]
    for numbers in new_list:
        if numbers > largest:
            largest = numbers

print(f"The largest number is {largest}")
