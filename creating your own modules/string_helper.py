def change_case(orig_string: str):
    if orig_string.isupper():
        new_string = orig_string.lower()
    elif orig_string.islower():
        new_string = orig_string.upper()
    else:
        new_string = orig_string.swapcase()
    return new_string

def split_in_half(orig_string: str):
    half = len(orig_string) // 2
    return orig_string[:half]

def remove_special_characters(orig_string: str):
    special_characters = [",", "!"]
    for character in special_characters:
        orig_string = orig_string.replace(character, "")
    return orig_string
