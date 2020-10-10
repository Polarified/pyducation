from euler.helpers import *

coefficients = (0, 0)
max_counter = 0
counter = 0
n = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        while True:
            val = n ** 2 + a * n + b
            if val >= 0 and is_prime(val):
                counter += 1
            else:
                break
        if counter > max_counter:
            coefficients = (a, b)


print(coefficients)