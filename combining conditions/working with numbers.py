numbers = []
negative = []
positive = []
print("Please type in integer numbers. Type in 0 to finish.")
ask = int(input("Number:"))
while True:
    if ask != 0:
        numbers.append(ask)
        ask = int(input("Number:"))
        if ask >= 0:
            positive.append(ask)
        if ask < 0:
            negative.append(ask)
    else:
        break
print(f"Numbers typed in {len(numbers)}")
sum = 0
for i in numbers:
    sum += i
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum / (len(numbers))}")
print(f"Positive numbers {len(positive)}")
print(f"Negative numbers {len(negative)}")

