def line(width, character, sign, height):
    print(character * width)

def shape(width, character, height, sign):
    n = 1
    while n <= width:
        line(n, character, sign, height)
        n += 1
    n = 1
    while n <= height:
        line(width, sign, sign, height)
        n += 1

# Examples
shape(5, "X", 3, "*")
print()
shape(2, "o", 4, "+")
print()
shape(3, ".", 0, ",")
