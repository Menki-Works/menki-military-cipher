---

```python
# Unit test for encryption/decryption

from core.symmetric import encrypt, decrypt
import os

def test_encrypt_decrypt():
    key = os.urandom(32)
    data = b"Secret military-grade text."
    nonce, ct = encrypt(data, key)
    pt = decrypt(nonce, ct, key)
    assert pt == data
