def formatted(my_list):
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = []
    for numbers in my_list:
        numbers = (f"{numbers:.2f}")
        new_list.append(numbers)
    print(new_list)
    return
if __name__=="__main__":
    formatted([1.234, 0.3333, 0.11111, 3.446])