from random import randint


def roll(die: str):
    result = []
    A = [3, 3, 3, 3, 3, 6]
    B = [2, 2, 2, 5, 5, 5]
    C = [1, 4, 4, 4, 4, 4]

    if die == "A":
        result.append(randint(0, len(A) - 1))
    elif die == "B":
        result.append(randint(0, len(B) - 1))
    elif die == "C":
        result.append(randint(0, len(C) - 1))

    return result


if __name__ == '__main__':
    for i in range(20):
        print(roll("A")[0], " ", end="")
    print()
    for i in range(20):
        print(roll("B")[0], " ", end="")
    print()
    for i in range(20):
        print(roll("C")[0], " ", end="")
