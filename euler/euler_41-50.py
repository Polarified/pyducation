from euler.helpers import *


# 41. Pandigital prime
@timer
def answer():
    for i in range(7654321, 0, -1):
        if is_pandigital(i) and is_prime(i):
            return i


print("41.", answer())


# 42. Coded triangle numbers
triangle_numbers = {int(i / 2 * (i + 1)) for i in range(1, 50)}
with open('p042_words.txt', 'r') as f:
    words = f.read().replace('"', '').split(',')
    answer = len([word for word in words if sum(ord(c) - 64 for c in word) in triangle_numbers])

print("42.", answer)
