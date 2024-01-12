def print_alternating_numbers():
    # Get user input for the upper limit
    number = int(input("Please type in a number: "))

    # Validate input
    if number <= 0:
        print("Please enter a positive number.")
        return

    # Initialize variables for alternating ends
    start = 1
    end = number

    # Print alternating numbers
    while start <= end:
        print(start)
        if start != end:
            print(end)
        start += 1
        end -= 1

# Call the function to run the program
print_alternating_numbers()
