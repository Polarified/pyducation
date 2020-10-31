import itertools
from euler.helpers import *

# 31. Coin sums


# 32. Pandigital products
a = {int(''.join(p[5:])) for p in itertools.permutations('123456789') if
     int(''.join(p[:2])) * int(''.join(p[2:5])) == int(''.join(p[5:]))}
b = {int(''.join(p[5:])) for p in itertools.permutations('123456789') if
     int(''.join(p[:1])) * int(''.join(p[1:5])) == int(''.join(p[5:]))}
answer = sum(a | b)
print("32.", answer)

# 33. Digit cancelling fractions


# 34. Digit factorials
answer = sum(i for i in range(10, 10000000) if i == sum(math.factorial(int(x)) for x in str(i)))
print("34.", answer)


# 35. Circular primes
answer = len([n for n in range(2, 1000000) if is_circular(n)])
print("35.", answer)

# 36. Double base palindromes
answer = sum(i for i in range(1000000) if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]))
print("36.", answer)

# 37. Truncatable primes
answer = sum(i for i in range(10, 1000000) if is_truncatable(i))
print("37.", answer)

# 38. Pandigital multiples
z = [''.join(i) for i in itertools.permutations('123456879')]
m = 0
for i in range(9, 10000):
    y = ''
    for j in range(1, 10):
        y += str(i * j)
        if len(y) >= 9:
            if len(y) == 9 and y in z:
                m = max(m, int(y))
            break

print("38.", m)

# 39. Integer right triangles
tmax = 0
answer = 0
for i in range(12, 1001):
    imax = 0
    for j in range(1, i // 3):
        for k in range(1, (i - j)//2 + 1):
            if (i - k - j) ** 2 == j ** 2 + k ** 2:
                imax += 1
    if imax > tmax:
        tmax = imax
        answer = i
print(answer)

# 40. Champernownes constant
answer = math.prod([int(('x' + ''.join(str(i) for i in range(1, 1000000)))[10 ** i]) for i in range(7)])
print("40.", answer)
