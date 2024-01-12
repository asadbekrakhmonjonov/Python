def longest_series_of_neighbours(lst):
    if not lst:
        return 0

    longest_length = 1
    current_length = 1

    for i in range(1, len(lst)):
        if abs(lst[i] - lst[i - 1]) == 1:
            current_length += 1
        else:
            current_length = 1

        longest_length = max(longest_length, current_length)

    return longest_length

# Example usage:
my_list = [1, 2, 5, 4, 3, 4]
result = longest_series_of_neighbours(my_list)
print(result)  # Output: 4
