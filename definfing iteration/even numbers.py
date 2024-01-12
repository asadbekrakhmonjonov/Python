""" Please write a function named even_numbers, which takes a list of integers as an argument. The function returns a new list containing the even numbers from the original list. """
def even_numbers(list):
    even = []
    for numbers in list:
        if numbers % 2 == 0:
            even.append(numbers)
    print(even)
if __name__=="__main__":
    even_numbers([1,2,3,4,5])