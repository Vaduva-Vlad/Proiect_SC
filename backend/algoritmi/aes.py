from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import unpad

def AES_encrypt(message,key,iv):
    message=bytes(message,'utf-8')
    key=bytes(key,'utf-8')
    cipher=AES.new(key,AES.MODE_CBC,iv)
    padded_message = message + (16 - len(message) % 16) * chr(16 - len(message) % 16).encode()
    encrypted_message = cipher.encrypt(padded_message)
    return encrypted_message.hex()

def AES_decrypt(message,key,iv):
    message=bytes.fromhex(message)
    key = bytes(key, 'utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    result=cipher.decrypt(message)
    return unpad(result,AES.block_size).decode('utf-8')

if __name__=="__main__":
    iv = get_random_bytes(16)
    encrypted=AES_encrypt('message','0000000000000000',iv)
    print(encrypted)
    print(AES_decrypt(encrypted,'0000000000000000',iv))