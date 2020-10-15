import itertools

# Pandigital products
# a = {int(''.join(p[5:])) for p in itertools.permutations('123456789') if
#      int(''.join(p[:2])) * int(''.join(p[2:5])) == int(''.join(p[5:]))}
# b = {int(''.join(p[5:])) for p in itertools.permutations('123456789') if
#      int(''.join(p[:1])) * int(''.join(p[1:5])) == int(''.join(p[5:]))}
# answer = sum(a | b)
# print("32.", answer)

# Digit cancelling fractions
for i in range(10, 99):
    for j in range(1, 11):
        pass
