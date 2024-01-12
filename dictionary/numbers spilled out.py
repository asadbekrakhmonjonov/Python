import inflect
def dict_of_numbers():
    p = inflect.engine()
    dictionary_numbers = {}
    for i in range(100):
        spell = p.number_to_words(i)
        dictionary_numbers[i] = spell
    return dictionary_numbers
numbers = dict_of_numbers()
print(numbers[2])
print(numbers[11])
print(numbers[45])
print(numbers[99])
print(numbers[95])