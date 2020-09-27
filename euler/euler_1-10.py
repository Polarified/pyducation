import math
import functools

# 1. Multiples of 3 and 5
answer = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
print("1.", answer)


# 2. Even value Fibonacci sum
@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


answer = sum(fib(x) for x in range(50) if fib(x) % 2 == 0 and fib(x) < 4000000)
print("2.", answer)


# 3. Largest prime factor
def prime_factors(n):
    factors = []
    for factor in range(2, int(math.sqrt(n)) + 1):
        while n % factor == 0:
            factors.append(factor)
            n /= factor
    return factors


answer = max(prime_factors(600851475143))
print("3.", answer)

# 4. Largest palindrome product
answer = max(x * y for x in range(100, 1000) for y in range(100, 1000) if str(x * y) == str(x * y)[::-1])
print("4.", answer)

# 5. Smallest multiple
answer = functools.reduce(lambda a, b: int(a * b / int(math.gcd(a, b))), range(1, 20))
print("5.", answer)

# 6. Sum square difference
answer = sum(range(1, 101)) ** 2 - sum(x ** 2 for x in range(1, 101))
print("6.", answer)


# 7. 10001st prime
# A cute, shorter, slower solution
# primes = [2]
# candidate = 1
# while len(primes) < 10001:
#     candidate += 2
#     remainders = [candidate % prime for prime in primes]
#     is_prime = all(remainders)
#     if is_prime:
#         primes.append(candidate)
# answer = primes[-1]
# print("7.", answer)

# A faster solution
def is_prime(n):
    for factor in range(2, int(math.sqrt(n)) + 1):
        if n % factor == 0 and n != factor:
            return False
    return True


count = 0
index = 2
answer = 0
while count < 10001:
    if is_prime(index):
        answer = index
        count += 1
    index += 1

print("7.", answer)

# 8. Largest product in a series
series = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
answer = max(math.prod(map(int, list(series[i:i + 13]))) for i in range(0, 1000 - 13 + 1))
print("8.", answer)

# 9. Special Pythagorean triplet
triplets = [(x, 1000 - x - y, y) for x in range(1, 999) for y in range(1, 1000 - x) if
            x < 1000 - x - y < y and x ** 2 + (1000 - x - y) ** 2 == y ** 2]
answer = math.prod(triplets[0])
print("9.", answer)


# 10. Summation of primes
def sieve(n):
    numbers = [True] * (n + 1)
    for i in range(2, int(math.sqrt(n) + 1)):
        if numbers[i]:
            for j in range(n):
                if i ** 2 + j * i > n:
                    break
                numbers[i ** 2 + j * i] = False
    return [i + 2 for i, n in enumerate(numbers[2:-1]) if n]


answer = sum(sieve(2000000))
print("10.", answer)
