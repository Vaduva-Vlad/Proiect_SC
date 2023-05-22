def ksa(key):
    schedule = [i for i in range(0, 256)]

    # Cream un array temporar pentru a avea un initial permutation pentru schedule
    t = []
    for k in range(0, 256):
        t.append(key[k % len(key)])

    i = 0
    for j in range(0, 256):
        i = (i + schedule[j] + t[j]) % 256
        schedule[i], schedule[j] = schedule[j], schedule[i]

    return schedule


def create_stream(schedule):
    j = 0
    i = 0
    while True:
        i = (i + 1) % 256
        j = (schedule[i] + j) % 256

        schedule[i], schedule[j] = schedule[j], schedule[i]

        yield schedule[(schedule[i] + schedule[j]) % 256]


def rc4_encrypt(message, key):
    message = [ord(c) for c in message]
    key = [ord(c) for c in key]

    schedule = ksa(key)
    stream = create_stream(schedule)

    result = ''
    for character in message:
        encrypted = str(hex(character ^ next(stream)))
        result += encrypted

    return result


def rc4_decrypt(message, key):
    message = message.split("0x")[1:]
    message = [int('0x' + c, 0) for c in message]
    key = [ord(c) for c in key]

    schedule = ksa(key)
    stream = create_stream(schedule)

    result = ''
    for character in message:
        encrypted = str(chr(character ^ next(stream)))
        result += encrypted

    return result


if __name__ == "__main__":
    s = [ord(c) for c in 'secret']
    print(ksa(s))
    enc = rc4_encrypt('message', 'secret')
    print(enc)
    print(rc4_decrypt(enc, 'secret'))
