import time
import math
import itertools
from operator import itemgetter
import decimal

from euler.helpers import *

answer = "BLANK"

# 21. Amicable numbers
# answer = sum(a + b for a in range(1, 10000) for b in range(1, 10000) if a != b and are_amicable(a, b))
print("21.", answer)

# 22. Name scores
names = sorted(open('p022_names.txt', 'r').read().replace('"', '').split(','))
scores = {name: (names.index(name) + 1) * sum(ord(c) - 64 for c in name) for name in names}
answer = sum(scores.values())
print("22.", answer)

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
def cycle_size(n):
    x = 0
    while True:
        x += 1
        if (10 ** x) % n == 1:
            return x


t = time.time()
answer = max(((i, cycle_size(i)) for i in range(2, 1000) if i % 5 != 0 and i % 2 != 0), key=itemgetter(1))[0]
print("26.", answer, time.time() - t)

# 28. Number spiral diagonals
answer = 1
d = 1
for i in range(500):
    for j in range(4):
        d += i * 2 + 2
        answer += d
print("28.", answer)

# 29. Distinct powers
answer = len(set(a ** b for a in range(2, 101) for b in range(2, 101)))
print("29.", answer)

# 30. Digit fifth powers
answer = sum([i for i in range(2, 10000000) if sum(x ** 5 for x in [int(y) for y in list(str(i))]) == i])
print("30.", answer)
