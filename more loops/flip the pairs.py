def flip_order_and_print(number):
    flipped_numbers = []

    # Generate the list of positive integers up to the given number
    original_numbers = list(range(1, number + 1))

    # Flip the order of each pair of numbers
    for i in range(1, number + 1, 2):
        if i + 1 <= number:
            flipped_numbers.extend([i + 1, i])
        else:
            flipped_numbers.append(i)

    # Print the flipped order
    for num in flipped_numbers:
        print(num)


# Get input from the user
user_input = int(input("Please type in a number: "))

# Call the function to flip the order and print
flip_order_and_print(user_input)

