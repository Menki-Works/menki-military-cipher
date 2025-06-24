from datetime import datetime
import json

def build_metadata(nonce: bytes, timestamp=None):
    if timestamp is None:
        timestamp = datetime.utcnow().isoformat()
    return json.dumps({
        "nonce": nonce.hex(),
        "timestamp": timestamp
    }).encode()
