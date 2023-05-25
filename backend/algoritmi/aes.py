from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def AES_encrypt(message,key):
    iv=get_random_bytes(16)
    cipher=AES.new(key,AES.MODE_CBC,iv)
    padded_message = message + (16 - len(message) % 16) * chr(16 - len(message) % 16).encode()
    encrypted_message = cipher.encrypt(padded_message)

    return encrypted_message.hex()