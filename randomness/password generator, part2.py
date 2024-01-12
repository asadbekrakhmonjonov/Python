from random import randint, shuffle

def generate_strong_password(length: int, use_special_chars: bool, use_numbers: bool):
    password = ['!', '?', '=', '+', '-', '()', '#']
    letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    password.extend(letters)

    if use_special_chars:
        password.extend(['!', '?', '=', '+', '-', '()', '#'])
    if use_numbers:
        password.extend([str(i) for i in range(1, 100)])

    shuffle(password)
    result = ''.join(password[:length])
    return result

if __name__ == '__main__':
    print(generate_strong_password(8, True, True))
