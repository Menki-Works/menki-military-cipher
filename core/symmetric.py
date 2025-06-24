from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def encrypt(data: bytes, key: bytes) -> tuple:
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ct = aesgcm.encrypt(nonce, data, None)
    return nonce, ct

def decrypt(nonce: bytes, ct: bytes, key: bytes) -> bytes:
    aesgcm = AESGCM(key)
    return aesgcm.decrypt(nonce, ct, None)
