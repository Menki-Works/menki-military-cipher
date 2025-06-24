import hmac
import hashlib

def compute_hmac(key: bytes, data: bytes) -> bytes:
    return hmac.new(key, data, hashlib.sha3_256).digest()

def verify_hmac(key: bytes, data: bytes, hmac_to_check: bytes) -> bool:
    return hmac.compare_digest(
        compute_hmac(key, data),
        hmac_to_check
    )
