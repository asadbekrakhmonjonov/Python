def squared(s, n):
    if n <= 0:
        print("Invalid value for n. Please use a positive integer.")
        return

    length = len(s)
    if length == 0:
        print("Empty string. Please provide a non-empty string.")
        return

    # Create the square
    for i in range(n):
        row = ""
        for j in range(n):
            index = (i * n + j) % length  # Corrected indexing
            row += s[index]
        print(row)

# Test cases
squared("abc", 5)
print()
squared("aybabtu", 5)
