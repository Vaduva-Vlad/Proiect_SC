from fastapi import FastAPI, Request
from algoritmi.rsa import *
from algoritmi.rc4 import *
import os

app = FastAPI()


@app.post("/api/encrypt/rsa")
async def rsa_encrypt(request: Request):
    data = await request.json()
    if not os.path.exists("public_key.txt"):
        save_keys()
    load_keys()
    message = data['message']
    return " ".join(encrypt(message))


@app.post("/api/decrypt/rsa")
async def rsa_decrypt(request: Request):
    data = await request.json()
    message = data['message']
    message=message.split(" ")
    message=[number for number in message]
    load_keys()
    return decrypt(message)

@app.post("/api/encrypt/rc4")
async def encrypt_rc4(request: Request):
    data = await request.json()
    message=data['message']
    key=data['key']

    return rc4_encrypt(message,key)

@app.post("/api/decrypt/rc4")
async def decrypt_rc4(request: Request):
    data = await request.json()
    message=data['message']
    key=data['key']

    return rc4_decrypt(message,key)