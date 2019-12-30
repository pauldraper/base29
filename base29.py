import string

BASE = 29
CHARS = "".join(c for c in string.digits + string.ascii_lowercase if c not in "01ailou")


def encode_number(number):
    result = ""
    while number:
        result += CHARS[number % BASE]
        number //= BASE
    return result[::-1]


def decode_number(chars):
    value = 0
    for c in reversed(chars):
        value *= BASE
        value += index(CHARS, c)
    return value


if __name__ == "__main__":
    import random

    for _ in range(10):
        number = random.randint(0, 2 ** 64 - 1)
        print("{:0>20}\t{:2>14}".format(number, encode_number(number)))
