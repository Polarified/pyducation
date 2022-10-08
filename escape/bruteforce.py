import hashlib
import string
import random
import itertools


def check_password(attempted_password: bytes):
    if len(attempted_password) != 10:
        return False
    if hashlib.md5(attempted_password).hexdigest() == '6ab0473b1b12d4bdd5e1f24325ab814c':
        return True


def main():
    while True:
        attempted_password = input('Enter the password: ')
        if check_password(attempted_password.encode('utf-8')):
            print('Correct!')
        else:
            print('Wrong.')


if __name__ == '__main__':
    main()


def unoptimized_random_attempt():
    while True:
        x = ''.join(random.choices(string.printable, k=5)).encode('utf-8')
        print(x)
        if check_password(x):
            break


def optimized_attempt(password_length):
    for f in string.digits[:password_length - 1]:
        for s in string.ascii_lowercase:
            for t in string.punctuation:
                attempted_password = f + int(f) * s + str(password_length - int(f) - 2) + (
                        password_length - int(f) - 2) * t
                if check_password(attempted_password.encode('utf-8')):
                    print('Yay!', attempted_password)


def product_loop(generator):
    for p in generator:
        if check_password(''.join(p).encode('utf-8')):
            print('\nPassword:', ''.join(p))
            return ''.join(p)
    return False


def unoptimized_attempt(password_length):
    all_char = string.digits + string.ascii_letters + string.punctuation

    generator = itertools.product(all_char, repeat=password_length)
    p = product_loop(generator)
    if p is not False:
        return p


optimized_attempt(10)
# unoptimized_attempt(10)
# unoptimized_random_attempt()
