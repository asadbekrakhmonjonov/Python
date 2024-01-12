""" Please write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, the program should print out a message accordingly.

In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the substring aa is at index 2.

 """
def find_second_occurrence(string, substring):
    first_occurrence = string.find(substring)

    if first_occurrence == -1:
        print("The substring does not occur twice in the string.")
    elif first_occurrence == len(string) - len(substring):
        print(f"The substring is at index {first_occurrence}. It occurs only once in the string.")
    else:
        second_occurrence = string.find(substring, first_occurrence + len(substring))

        if second_occurrence == -1:
            print("The substring does not occur twice in the string.")
        else:
            print(f"The second occurrence of the substring is at index {second_occurrence}.")

# Get input from the user
user_string = input("Please type in a string: ")
user_substring = input("Please type in a substring: ")

# Call the function
find_second_occurrence(user_string, user_substring)
