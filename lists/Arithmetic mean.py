def mean(my_list):
    sum = 0
    res = 0
    for numbers in my_list:
        sum += numbers
        res = sum / len(my_list)
    return res
my_list = [1, 2, 3,4,5]
result = mean(my_list)
print("mean value is", result)



