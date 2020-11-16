from collections import Counter
from itertools import zip_longest
from pprint import pprint

KEYLENGTH = 6
COMMON = 'ETAOINSRHDLUCMFYWGPBVKXQJZ'
CIPHER = 'HCIKVRJOX'


def get_mappings(datapath):
    with open(datapath, 'r') as data:
        ciphertext = data.read().replace(" ", "")
        segments = [ciphertext[i::KEYLENGTH] for i in range(KEYLENGTH)]
        pprint(segments)
        commons = [Counter(segment).most_common() for segment in segments]
        pprint(commons)
        orders = [''.join([c[0] for c in common]) for common in commons]
        mappings = [{x: y for x, y in zip_longest(order, COMMON, fillvalue='-')} for order in orders]
        alphamappings = [{k: v for k, v in sorted(mapping.items())} for mapping in mappings]
        return orders, mappings, alphamappings


def print_rotations():
    for i in range(26):
        print(i, ''.join([chr((((ord(c) - ord("A")) + i) % 26) + ord("A")) for c in COMMON]))


def solve(mappings, cipher):
    plain = ''.join([mappings[index % KEYLENGTH][c] for index, c in enumerate(cipher)])
    return plain


def better_solve():
    """
    Need to figure out the rotation for each position in the key. This is like looking at COMMON vs ORDER and figuring out what the rotation should be.
    I could do this by creating all possible rotations for COMMON and figuring out which of the rotations looks most like each ORDER.
    """


def main():
    orders, mappings, alphamappings = get_mappings('data')
    for i in range(KEYLENGTH):
        print("ORDER:", orders[i])
        print("COMMON", COMMON)
        # print("FREQUENT:", mappings[i])
        # print("ALPHA:", alphamappings[i])
    plain = solve(mappings, CIPHER)
    print(plain)

    print_rotations()


main()
