import random


def password_generator(length=8):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alphabet_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    password = ''

    while len(password) < length:
        if random.randrange(0, 100, 1) % 3 == 0:
            password += alphabet[random.randrange(0, len(alphabet), 1)]
        if random.randrange(0, 100, 1) % 4 == 0:
            password += alphabet_low[random.randrange(0, len(alphabet_low), 1)]
        if random.randrange(0, 100, 1) % 5 == 0:
            password += numbs[random.randrange(0, len(numbs), 1)]

    return password
