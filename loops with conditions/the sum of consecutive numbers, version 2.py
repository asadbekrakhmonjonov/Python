def calculate_sum_with_steps(limit):
    current_sum = 0
    i = 1
    steps = []

    while current_sum < limit:
        current_sum += i
        steps.append(str(i))
        i += 1

    return current_sum, steps

def main():
    try:
        limit = int(input("Enter the limit: "))
        result, steps = calculate_sum_with_steps(limit)

        # Displaying the calculation steps
        calculation_str = " + ".join(steps)
        print(f"The consecutive sum: {calculation_str} = {result}")

    except ValueError:
        print("Please enter a valid integer for the limit.")

if __name__ == "__main__":
    main()