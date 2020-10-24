import math
import itertools
from euler.helpers import *

# 31. Coin sums


# 32. Pandigital products
# a = {int(''.join(p[5:])) for p in itertools.permutations('123456789') if
#      int(''.join(p[:2])) * int(''.join(p[2:5])) == int(''.join(p[5:]))}
# b = {int(''.join(p[5:])) for p in itertools.permutations('123456789') if
#      int(''.join(p[:1])) * int(''.join(p[1:5])) == int(''.join(p[5:]))}
# answer = sum(a | b)
# print("32.", answer)

# 33. Digit cancelling fractions
# for i in range(10, 99):
#     for j in range(1, 11):
#         pass

# 34. Digit factorials
# answer = sum(i for i in range(10, 10000000) if i == sum(math.factorial(int(x)) for x in str(i)))
# print("34.", answer)


# 35. Circular primes
# answer = len([n for n in range(2, 1000000) if is_circular(n)])
# print("35.", answer)

# 36. Double base palindromes
# answer = sum(i for i in range(1000000) if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]))
# print("36.", answer)

# 37. Truncatable primes
answer = sum(i for i in range(10, 1000000) if is_truncatable(i))
print("37.", answer)
