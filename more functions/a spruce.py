def spruce(size):
    s = 1
    n = 1
    f = size - 1
    print("a spruce!")
    while n <= size:
        print(" " * f + "*" * s)
        s += 2
        n += 1
        f -= 1
    print(" "* (size - 1) + "*")
spruce(3)