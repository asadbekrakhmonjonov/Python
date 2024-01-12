def main():
    words = set()  # Set to store unique words
    count = 0

    while True:
        word = input("Word: ").strip().lower()  # Convert the input to lowercase for case-insensitivity

        if word in words:
            break
        else:
            words.add(word)
            count += 1

    print(f"You typed in {count} different {'word' if count == 1 else 'words'}.")

if __name__ == "__main__":
    main()
