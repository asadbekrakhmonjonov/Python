""" Please write a program which asks the user for a password. The program should then ask the user to type in the password again. If the user types in something else than the first password, the program should keep on asking until the user types the first password again correctly.

 """
# Write your solution here
password1 = input("Password:")
password2 = input("Repeat password:")
while True:
    if password1 != password2:
        print("They do not match!")
        password2 = input("Repeat password:")
    else:
        break
print("User account created!")
