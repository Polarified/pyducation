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

# 43. Sub-string divisibility
pandigitals = [n for n in map(''.join, itertools.permutations('0123456789'))]
answer = sum([int(n) for n in pandigitals if is_subtring_divisibile(n)])
print("43.", answer)

# 44. Pentagon numbers
pentagonals = {pentagonal(n) for n in range(1020, 15000)}
p = [(i, j) for i, j in itertools.combinations(pentagonals, 2) if i + j in pentagonals and abs(i - j) in pentagonals]
pj, pk = p[0]
print("44.", abs(pj - pk))

# 45. Triangular, pentagonal, hexagonal
t = {triangular(n) for n in range(1, 100000)}
p = {pentagonal(n) for n in range(1, 100000)}
h = {hexagonal(n) for n in range(1, 100000)}
commons = {x for x in t if x in p and x in h}
print("45.", commons)

# 46. Goldbach's other conjecture
# Very inefficient. Requires some math to make better.
odds = {n for n in range(2, 10000) if n % 2 == 1}
primes = set(sieve_of_eratosthenes(10000))
odd_composites = odds - primes
oc = sorted(list(odd_composites))
for n in oc:
    print('Started searching for', n)
    try:
        for p in primes:
            for k in range(1, n // 2):
                if n == p + 2 * (k ** 2):
                    print('Found solution: {} = {} + 2x{}^2'.format(n, p, k))
                    raise KeyboardInterrupt
    except KeyboardInterrupt:
        continue
    print("Couldn't find solution for ", n)
    answer = n
    break
print("46.", answer)
