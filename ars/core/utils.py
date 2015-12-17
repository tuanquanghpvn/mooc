from django.conf import settings
from itertools import cycle


# Encryption
def encryption(message):
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(message, cycle("ABC!@#abc^%$#@!")))


# Decryption
def decryption(message):
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(message, cycle("ABC!@#abc^%$#@!")))