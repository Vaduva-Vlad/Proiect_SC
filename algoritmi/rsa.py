from math import sqrt, gcd
from random import randint

private_key=None
public_key=()
n=None

def isprime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    for i in range(2, int(sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def generate_prime_numbers():
    p = randint(1000, 10000)
    q = randint(1000, 10000)
    while p==q or not (isprime(p) and isprime(q)):
        p = randint(1000, 10000)
        q = randint(1000, 10000)
    return p, q


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
    p, q = generate_prime_numbers()

    global n
    n = p * q
    fi = (p - 1) * (q - 1)

    e = get_e(fi)

    global private_key
    global public_key
    private_key = get_d(e, fi)

    public_key = (n, e)


def encrypt(message):
    encoded = [ord(c) for c in message]

    n=public_key[0]
    e=public_key[1]

    result=[]

    for letter in encoded:
        encrypted_letter=1
        e = public_key[1]
        while e>0:
            encrypted_letter*=letter
            encrypted_letter%=n
            e-=1
        result.append(str(encrypted_letter))

    return result

def decrypt(message):
    result=[]

    for number in message:
        number=int(number)
        d = private_key
        decrypted=1
        while d>0:
            decrypted*=number
            decrypted%=n
            d-=1
        result.append(chr(decrypted))

    return result

if __name__=="__main__":
    get_keys()
    with open('public_key.txt','w') as f:
        f.write(f"{str(public_key[0])}\n")
        f.write(f"{str(public_key[1])}\n")
        f.write(str(private_key))

    enc=encrypt('mesaj')

    with open('public_key.txt','r') as f:
        lines=f.readlines()
        private_key=int(lines[2])

    print(decrypt(enc))