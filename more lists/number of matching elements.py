def count_matching_elements(my_matrix: list,element: int):
    count = 0
    for i in range(len(my_matrix)):
        for j in range(len(my_matrix)):
            if element == my_matrix[i][j]:
                count += 1
    return count
m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
print(count_matching_elements(m, 1))
