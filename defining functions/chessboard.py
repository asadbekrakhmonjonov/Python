def chessboard(size):
    for i in range(size):
        row = ""
        for j in range(size):
            # Swap 0 and 1 to correct the chessboard pattern
            row += str((i + j) % 2 ^ 1)
        print(row)

# Examples
print("Chessboard with size 3:")
chessboard(3)
print()

print("Chessboard with size 6:")
chessboard(6)
