def create_tuple(x: int,y: int,z: int):
    tuple = ([],[],[])
    if y > x < z:
        tuple[0].append(x)
    elif x > y < z:
        tuple[0].append(y)
    elif x > z < y:
        tuple[0].append(z)
    if y < x > z:
        tuple[1].append(x)
    elif x < y > z:
        tuple[1].append(y)
    elif x < z > y:
        tuple[1].append(z)
    sum = x + y + z
    tuple[2].append(sum)
    return tuple
if __name__ == "__main__":
    print(create_tuple(5, 3, -1))



