# Write your solution here
year = int(input("Year:"))
while True:
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print(f"The next leap year after {year} is {year + 4}")
        break
    else:
        print(f"The next leap year after {year} is {year + 1}")
        break