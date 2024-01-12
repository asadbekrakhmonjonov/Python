def print_square(layers):
    if layers > 26:
        print("Error: Number of layers cannot exceed 26.")
        return

    for i in range(layers):
        line = ""
        for j in range(layers):
            char = chr(ord('A') + min(i, j, layers - i - 1, layers - j - 1))
            line += char
        print(line)


# Get input from the user
layers = int(input("Enter the number of layers: "))

# Print the square
print_square(layers)
