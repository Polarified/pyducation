from euler.helpers import *
import timeit


# 41. Pandigital prime

@timer
def x():
    for i in range(87654321, 12345678, -1):
        if is_pandigital(i) and is_prime(i):
            return i


print(x())
