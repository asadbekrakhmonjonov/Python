def hypotenuse(leg1:float,leg2:float):
    from math import sqrt
    length = (leg1 * leg1) + (leg2 * leg2)
    return sqrt(length)
if __name__ == '__main__':
    print(hypotenuse(3, 4))
    print(hypotenuse(5, 12))
    print(hypotenuse(1, 1))