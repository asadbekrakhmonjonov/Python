from random import shuffle

def generate_password(length: int):
    letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    shuffle(letters)
    password = ''.join(letters[:length])
    return password

if __name__ == '__main__':
    for i in range(10):
        print(generate_password(8))
