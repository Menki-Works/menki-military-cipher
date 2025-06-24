from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def derive_shared_key(private_key, peer_public_key):
    shared = private_key.exchange(peer_public_key)
    return HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'menki-session'
    ).derive(shared)

def hybrid_encrypt(plaintext: bytes, aes_key: bytes) -> tuple:
    aesgcm = AESGCM(aes_key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)
    return nonce, ciphertext

def hybrid_decrypt(ciphertext: bytes, nonce: bytes, aes_key: bytes) -> bytes:
    aesgcm = AESGCM(aes_key)
    return aesgcm.decrypt(nonce, ciphertext, None)
