import math
import itertools
from operator import itemgetter
import decimal

from euler.helpers import *


# 24. Lexicographic permutations
answer = list(itertools.permutations(range(10)))[999999]
print("24.", answer)

# 25. 1000-digit Fibonacci number
f1 = 1
f2 = 1
f = 2
i = 2
while len(str(f)) < 1000:
    f = f1 + f2
    f1 = f2
    f2 = f
    i += 1
answer = i
print("25.", answer)

# 26. Reciprocal cycles
decimal.getcontext().prec = 10
fractions = [1 / decimal.Decimal(i) for i in range(2, 1000)]
print(fractions)
