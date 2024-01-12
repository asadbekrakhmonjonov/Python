def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

while True:
    try:
        user_input = int(input("Please type in a number: "))
        if user_input <= 0:
            print("Thanks and bye!")
            break
        else:
            result = factorial(user_input)
            print(f"The factorial of the number {user_input} is {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")