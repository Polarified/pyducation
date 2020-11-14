from euler.helpers import *


# Need to use itertools.combinations_with_replacement, might help
def ways_to_make(n):
    if n == 1:
        return {1}
    if n == 2:
        return {2, (1, 1)}
    if n == 5:
        return {{ways_to_make(2)} | {ways_to_make(2)} | ways_to_make(1)}
    if n == 10:
        return 11
    if n == 20:
        return 20
    if n == 50:
        return 40
    if n == 100:
        return 82
    if n == 200:
        return 164


"""
1 -> 1.
2 -> 1, 1 / 2.
5 -> 2, 2, 1 / 5.
1 1 1 1 1
2 1 1 1
2 2 1
5
10 -> 5, 5 / 2, 2, 2, 2, 2/ 10
1 1 1 1 1 1 1 1 1 1
2 1 1 1 1 1 1 1 1
2 2 1 1 1 1 1 1
2 2 2 1 1 1 1
2 2 2 2 1 1
5 2 2 1
5 2 1 1 1
5 1 1 1 1 1
5 5
2 2 2 2 2
10



So to make 10, we have this many ways:

"""

print(is_subtring_divisibile('0406357289'))
