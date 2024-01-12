def statistics():
    numbers = input("Exam points and exercises completed:")
    numbers = numbers.split()
    points = int(numbers[0])
    exercises = int(numbers[1])

    results = points + (exercises // 10)

    if 0 < results <= 14:
        print("Grade is 0. Fail")
    elif 15 < results <= 17:
        print("Grade is 1")
    elif 18 < results <= 20:
        print("Grade is 2")
    elif 21 < results <= 23:
        print("Grade is 3")
    elif 24 < results <= 27:
        print("Grade is 4")
    elif 28 < results <= 30:
        print("Grade is 5")
    else:
        print("Invalid input. Please enter valid points and exercises.")


statistics()
