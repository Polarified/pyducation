username = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
password = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

import bz2

print(bz2.decompress(username))
print(bz2.decompress(password))

fly = 'bee' * 14
fly = fly.encode('utf-8')


def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


def single_char_xor(input_bytes, char_value):
    return ''.join([chr(byte ^ char_value) for byte in input_bytes])


# print(byte_xor(fly, password))
