# semantic_crypto_v37.py — lexical watermark (HMAC-based), self-contained
import re, hmac, hashlib

PAIRS = [
    ("start","begin"), ("end","finish"), ("big","large"), ("small","little"),
    ("use","utilize"), ("help","assist"), ("show","demonstrate"), ("need","require"),
    ("try","attempt"), ("get","obtain"), ("make","create"), ("part","component"),
    ("idea","concept"), ("goal","objective"), ("safe","secure"), ("right","correct"),
    ("test","examination"), ("work","operate"), ("fast","rapid"), ("slow","gradual")
]

WORD_RE = re.compile(r"\b\w+\b")

def _bits_from_key(key: bytes, text: str, nbits: int):
    data = hmac.new(key, text.encode('utf-8'), hashlib.sha256).digest()
    out_bits = []
    buf = data
    while len(out_bits) < nbits:
        for byte in buf:
            for i in range(8):
                out_bits.append((byte >> i) & 1)
                if len(out_bits) >= nbits:
                    break
            if len(out_bits) >= nbits:
                break
        buf = hashlib.sha256(buf).digest()
    return out_bits[:nbits]

def embed(text: str, key: str):
    key_b = key.encode('utf-8')
    tokens = WORD_RE.findall(text)
    lower = [t.lower() for t in tokens]
    positions = []
    for i,t in enumerate(lower):
        for pi,(w0,w1) in enumerate(PAIRS):
            if t==w0 or t==w1:
                positions.append((i,pi))
                break
    nbits = len(positions)
    bits = _bits_from_key(key_b, text, nbits)
    out = tokens[:]
    applied=0
    for (idx,pi),bit in zip(positions,bits):
        w0,w1 = PAIRS[pi]
        orig = out[idx]
        des = w0 if bit==0 else w1
        out[idx] = des.capitalize() if orig and orig[0].isupper() else des
        applied+=1
    # Reconstruct text by replacing sequential word matches
    i=0
    def repl(m):
        nonlocal i
        val = out[i]; i+=1; return val
    new_text = WORD_RE.sub(repl, text)
    return new_text, {"candidates":nbits,"applied":applied}

def detect(text: str, key: str):
    key_b = key.encode('utf-8')
    tokens = WORD_RE.findall(text)
    lower=[t.lower() for t in tokens]
    obs_bits=[]
    for t in lower:
        for w0,w1 in PAIRS:
            if t==w0: obs_bits.append(0); break
            if t==w1: obs_bits.append(1); break
    nbits = len(obs_bits)
    exp_bits = _bits_from_key(key_b, text, nbits)
    matches = sum(1 for o,e in zip(obs_bits,exp_bits) if o==e)
    rate = (matches/nbits) if nbits>0 else 0.0
    return {"observed_bits": nbits, "matches": matches, "rate": rate}
