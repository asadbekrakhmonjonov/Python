def histogram(word: str):
    groups = {}
    for letter in word:
        if letter not in groups:
            groups[letter] = []
        groups[letter].append(letter)
    return groups

word = "example"  # Replace this with your desired word
result = histogram(word)

for key, value in result.items():
    print(f"{key}",end=" ")
    for letter in value:
        print("*")
