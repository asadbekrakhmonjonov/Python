""" Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321. The program should then print out the number of times the user tried different codes. """
# Write your solution here
code = 4321
guess_count = 1
while True:
    guess = int(input("PIN:"))
    if code != guess:
        print("Wrong")
        guess_count += 1
    else:
        if guess_count == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {guess_count} attempts")
        break
