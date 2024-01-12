""" Generally, any year that is divisible by four is a leap year. However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400.

Please write a program which asks the user for a year, and then prints out whether that year is a leap year or not. """
# Write your solution here
def is_leap_year(year):
    # Leap years are divisible by 4
    # However, years divisible by 100 are not leap years, unless they're also divisible by 400
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def find_next_leap_year(year):
    while True:
        year += 1
        if is_leap_year(year):
            return year

user_year = int(input("Enter a year: "))

if is_leap_year(user_year):
    next_leap_year = find_next_leap_year(user_year)
    print(f"The next leap year after {user_year} is {next_leap_year}")
else:
    next_leap_year = find_next_leap_year(user_year - 1)
    print(f"The next leap year after {user_year} is {next_leap_year}")