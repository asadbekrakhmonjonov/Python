""" Please write a program which asks for the hourly wage, hours worked, and the day of the week. The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.
 Hourly wage: 8.5
Hours worked: 3
Day of the week: Monday
Daily wages: 25.5 euros """

# Write your solution here
hourly = float(input("\nHourly wage:\t"))
hours = int(input("\nHours worked: \t"))
day = input("\nDay of the week:\t ")
daily1 = hourly * hours
daily2 = hourly * hours * 2
if day == "Monday":
    print(f"\nDaily wages: {daily1} euros")
if day == "Tuesday":
    print(f"\nDaily wages: {daily1} euros")
if day == "Wednesday":
    print(f"\nDaily wages: {daily1} euros")
if day == "Thursday":
    print(f"\nDaily wages: {daily1} euros")
if day == "Friday":
    print(f"\nDaily wages: {daily1} euros")
if day == "Saturday":
    print(f"\nDaily wages: {daily1} euros")
if day == "Sunday":
    print(f"\nDaily wages: {daily2} euros")