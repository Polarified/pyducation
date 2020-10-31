import itertools
import math
import functools
import time
import numpy as np


@functools.lru_cache(maxsize=None)
def fib(n):
    """
    Finds the nth fibonacci series member.
    Caching reduces work.
    """
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def trial_division_factorization(n):
    """
    Returns list of all integer factors of n, using trial division.
    """
    return [factor for factor in range(1, int(n / 2) + 1) if n % factor == 0] + [n]


def improved_factorization(n, inclusive=True):
    factors = [item for subset in [{i, int(n / i)} for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0] for item in
               subset]
    if inclusive:
        return factors
    else:
        return sorted(factors)[:-1]


def prime_factors(n):
    """
    Finds all prime factors of a number n.
    """
    factors = []
    for factor in range(2, int(math.sqrt(n)) + 1):
        while n % factor == 0:
            factors.append(factor)
            n /= factor
    return factors


def is_prime(n):
    """
    Primality check for a number n.
    """
    if n == 1:
        return False
    for factor in range(2, int(math.sqrt(n)) + 1):
        if n % factor == 0 and n != factor:
            return False
    return True


def are_coprime(a, b):
    """
    Coprime check for two numbers a, b.
    """
    return math.gcd(a, b) == 1


def sieve_of_eratosthenes(n):
    """
    Finds all primes below a certain number n.
    """
    numbers = np.ones(n)
    for i in range(2, int(np.ceil(np.sqrt(n)))):
        if numbers[i]:
            for j in range(i * i, n, i):
                numbers[j] = 0
    return [i for i in range(2, len(numbers)) if numbers[i]]


def lcm(*args):
    """
    Finds the least common multiple of a sequence.
    """
    return functools.reduce(lambda a, b: int(a * b / int(math.gcd(a, b))), *args)


@functools.lru_cache(maxsize=None)
def are_amicable(a, b):
    """
    Amicability check for two integers a, b
    Amicable == Sum of proper divisors is equal.
    """
    return a != b and sum(improved_factorization(a)) == b and sum(improved_factorization(b)) == a


def is_perfect(n):
    """
    Perfection test for integer n
    A perfect number is one where the sum of proper divisors is equal to the number itself.
    """
    return n == sum(improved_factorization(n, inclusive=False))


def is_deficient(n):
    return n > sum(improved_factorization(n, inclusive=False))


def is_abundant(n):
    return n < sum(improved_factorization(n, inclusive=False))


@functools.lru_cache(maxsize=None)
def collatz(n):
    sequence = []
    while n > 1:
        sequence.append(int(n))
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence


def rotations(n):
    return [int(str(n)[i:] + str(n)[:i]) for i in range(len(str(n)))]


def is_circular(n):
    return all(map(is_prime, rotations(n)))


def is_palindrome(n):
    return str(n)[::-1] == str(n)


def truncations(n):
    return {int(str(n)[i:]) for i in range(len(str(n)))} | {int(str(n)[:i]) for i in range(1, len(str(n)))}


def is_truncatable(n):
    return all(map(is_prime, truncations(n)))


def is_pandigital(n):
    for i in range(1, len(str(n)) + 1):
        if str(i) not in str(n):
            return False
    return True


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed = toc - tic
        print(f"Elapsed time: {elapsed:0.4f} seconds")
        return value

    return wrapper_timer
