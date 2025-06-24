import sys
from core import keygen, hybrid_encrypt, symmetric, hash_verify, metadata

def demo():
    private, public = keygen.generate_keypair()
    print("Generated keypair.")
    keygen.save_keys(private, public)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        demo()
    else:
        print("Usage: python cli/main.py demo")
