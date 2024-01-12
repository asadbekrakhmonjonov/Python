""" Please write a function named sum_of_positives, which takes a list of integers as its argument. The function returns the sum of the positive values in the list. """
def sum_of_positives(list):
    sum = 0
    for numbers in list:
        if numbers >= 0:
            sum += numbers
    print(f"The result is {sum}")
    return sum
sum_of_positives([1,2,3,-5,-6])