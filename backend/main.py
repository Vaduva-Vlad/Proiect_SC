from fastapi import FastAPI, Request
from algoritmi.rsa import *
from algoritmi.rc4 import *
from algoritmi.aes import *
import os
from fastapi.middleware.cors import CORSMiddleware
from Crypto.Random import get_random_bytes

app = FastAPI()

origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

iv=get_random_bytes(16)

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

    with open('rc4_key.txt','w') as f:
        f.write(key)

    return rc4_encrypt(message,key)

@app.post("/api/decrypt/rc4")
async def decrypt_rc4(request: Request):
    data = await request.json()
    message=data['message']
    key=data['key']

    return rc4_decrypt(message,key)

@app.post("/api/encrypt/aes")
async def encrypt_aes(request: Request):
    data = await request.json()
    message = data["message"]
    key = data["key"]

    with open('aes_key.txt','w') as f:
        f.write(key)
    return AES_encrypt(message,key,iv)

@app.post("/api/decrypt/aes")
async def decrypt_aes(request: Request):
    data = await request.json()
    message = data["message"]
    key = data["key"]

    return AES_decrypt(message,key,iv)