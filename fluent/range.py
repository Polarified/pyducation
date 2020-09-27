"""
Iterable for an Arithmetic progression.
"""

import time
from decimal import Decimal
from fractions import Fraction


class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        forever = self.end is None
        result = type(self.begin + self.end)(self.begin)
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + index * self.step


a = ArithmeticProgression(1000, -10, 0)
for i in a:
    time.sleep(0.1)
    print(i)
