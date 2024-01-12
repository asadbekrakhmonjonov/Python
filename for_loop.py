import cowsay
def game():
    guess_count = 0
    guess_limit = 3

    while guess_count < guess_limit:
        guess = input("\nIt is the most important feeling: \t")
        guess_count += 1

        if guess.lower() == "love":
            print(f"\nNumber of tries: {guess_count}")
            answer = input("\nYou win, do you want to play again?\t ").lower()
            if answer == "yes":
                print(cowsay.cow("Let's nail it! "))
                game()
            else:
                print(cowsay.cow("\nSee you soon"))
            return

        else:
            if guess_count < guess_limit:
                print(f"\nNumber of tries: {guess_count}")
                print(f"\nTry again!\n")
            else:
                print(f"\nNumber of tries: {guess_count}")
                print("\nYou are out of tries\n")
                answer = input("\nYou lose, do you want to play again? \t").lower()
                if answer == "yes":
                    game()
                else:
                    print("Game over")
                return

game()





