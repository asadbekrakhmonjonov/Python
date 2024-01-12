""" Please write a program which asks the user to type in a limit. The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user.  """
limit = int(input("Limit: "))
current_sum = 0
i = 1
while current_sum < limit:
    current_sum = current_sum + i
    i += 1

print(current_sum)
