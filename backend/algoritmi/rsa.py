from math import sqrt, gcd
from random import randint

prime_numbers = []
private_key = []
public_key = []
n = None


def isprime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    for i in range(2, int(sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def sieve_of_eratosthenes():
    sieve = [True for i in range(250)]
    sieve[0] = False
    sieve[1] = False

    for i in range(2, 250):
        for j in range(i * 2, 250, i):
            sieve[j] = False

    for i in range(len(sieve)):
        if sieve[i]:
            prime_numbers.append(i)


def generate_prime_number():
    num = randint(0, len(prime_numbers) - 1)

    number = prime_numbers[num]
    prime_numbers.pop(num)
    return number


def get_e(fi):
    e = 2
    while gcd(e, fi) != 1:
        e += 1
    return e


def get_d(e, fi):
    d = 2
    while (d * e) % fi != 1:
        d += 1
    return d


def get_keys():
    sieve_of_eratosthenes()
    p = generate_prime_number()
    q = generate_prime_number()

    global n
    n = p * q
    fi = (p - 1) * (q - 1)

    e = get_e(fi)

    global private_key
    global public_key
    private_key = [get_d(e, fi)]

    public_key = [n, e]


def encrypt(message):
    encoded = [ord(c) for c in message]

    n = public_key[0]
    e = public_key[1]

    result = []

    for letter in encoded:
        encrypted_letter = 1
        e = public_key[1]
        while e > 0:
            encrypted_letter *= letter
            encrypted_letter %= n
            e -= 1
        result.append(str(encrypted_letter))

    return result


def decrypt(message):
    result = []
    n=public_key[0]

    for number in message:
        number = int(number)
        d = private_key[0]
        decrypted = 1
        while d > 0:
            decrypted *= number
            decrypted %= n
            d -= 1
        result.append(chr(decrypted))

    return "".join(result)


def save_keys():
    get_keys()
    with open('public_key.txt', 'w') as f:
        f.write(f"{str(public_key[0])}\n")
        f.write(f"{str(public_key[1])}\n")
        f.write(str(private_key[0]))


def load_keys():
    with open('public_key.txt', 'r') as f:
        lines = f.readlines()
        public_key.append(int(lines[0]))
        public_key.append(int(lines[1]))
        private_key.append(int(lines[2]))


if __name__ == "__main__":
    load_keys()
    print(private_key)
