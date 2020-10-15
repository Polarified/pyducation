
import itertools

# Pandigital products
# a = {int(''.join(p[5:])) for p in itertools.permutations('123456789') if
#      int(''.join(p[:2])) * int(''.join(p[2:5])) == int(''.join(p[5:]))}
# b = {int(''.join(p[5:])) for p in itertools.permutations('123456789') if
#      int(''.join(p[:1])) * int(''.join(p[1:5])) == int(''.join(p[5:]))}
# answer = sum(a | b)
# print("32.", answer)

# Digit cancelling fractions
for i in range(10, 99):
    for j in range(1, 11):
        pass

from euler.helpers import *


# 31. Coin sums
def ways_to_make(n):
    """
    Calculate how many ways there are to make a certain currency, using recursion and then multiplying.
    :param n:
    :return:
    """
    if n == 1:
        return 1
    elif n == 2 or n == 20 or n == 200:
        return {(ways_to_make(n / 2), ways_to_make(n / 2))} | {n}
    elif n == 5 or n == 50:
        return {(ways_to_make(n * 0.4), ways_to_make(n * 0.4), ways_to_make(n * 0.2))} | {n}
    elif n == 10 or n == 100:
        return ways_to_make(n / 2) | ways_to_make(n / 2) | {n, (n / 5, n / 5, n / 5, n / 5)}


print(ways_to_make(5))
