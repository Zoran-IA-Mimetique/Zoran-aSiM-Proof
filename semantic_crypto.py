# semantic_crypto.py (v36)
# Lexical semantic watermarking with HMAC-derived bitstream.
import re, hmac, hashlib, json

PAIRS = [
    ("start","begin"),
    ("end","finish"),
    ("big","large"),
    ("small","little"),
    ("use","utilize"),
    ("help","assist"),
    ("show","demonstrate"),
    ("need","require"),
    ("try","attempt"),
    ("get","obtain"),
    ("make","create"),
    ("part","component"),
    ("idea","concept"),
    ("goal","objective"),
    ("safe","secure"),
    ("right","correct"),
    ("test","examination"),
    ("work","operate"),
    ("fast","rapid"),
    ("slow","gradual")
]

WORD_RE = re.compile(r"\b\w+\b")

def _bits_from_key(key: bytes, text: str, nbits: int):
    data = hmac.new(key, text.encode('utf-8'), hashlib.sha256).digest()
    # extend by re-hashing if needed
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
    # Count how many candidate pairs occur
    tokens = WORD_RE.findall(text)
    # Build a mapping from lower-case to original forms (positions)
    lower_tokens = [t.lower() for t in tokens]
    positions = []  # [(index, which_pair, which_side)]
    pair_map = {}
    for idx, t in enumerate(lower_tokens):
        for pi, (w0, w1) in enumerate(PAIRS):
            if t == w0 or t == w1:
                positions.append((idx, pi))
                break
    nbits = len(positions)
    bits = _bits_from_key(key_b, text, nbits)
    # Apply replacements on the original text by reconstructing from tokens with spaces
    out_tokens = tokens[:]
    applied = 0
    for (pos_i, pair_i), bit in zip(positions, bits):
        w0, w1 = PAIRS[pair_i]
        original = out_tokens[pos_i]
        # Preserve casing
        def with_case(src, ref):
            return src.capitalize() if ref[0].isupper() else src
        desired = w0 if bit==0 else w1
        out_tokens[pos_i] = with_case(desired, original)
        applied += 1
    # Rebuild text by replacing tokens in sequence
    out_text = text
    # Replace by walking through matches, careful to keep punctuation
    def repl_iter(orig_text, new_tokens):
        i = 0
        def repl(m):
            nonlocal i
            rep = new_tokens[i]
            i += 1
            return rep
        return WORD_RE.sub(repl, orig_text)
    out_text = repl_iter(text, out_tokens)
    return out_text, {"candidates": nbits, "applied": applied}

def detect(text: str, key: str):
    key_b = key.encode('utf-8')
    tokens = WORD_RE.findall(text)
    lower_tokens = [t.lower() for t in tokens]
    obs_bits = []
    pair_idx = []
    for t in lower_tokens:
        found = False
        for pi,(w0,w1) in enumerate(PAIRS):
            if t == w0:
                obs_bits.append(0); pair_idx.append(pi); found=True; break
            if t == w1:
                obs_bits.append(1); pair_idx.append(pi); found=True; break
        # ignore tokens not in pairs
    nbits = len(obs_bits)
    exp_bits = _bits_from_key(key_b, text, nbits)
    matches = sum(1 for o,e in zip(obs_bits, exp_bits) if o==e)
    rate = (matches/nbits) if nbits>0 else 0.0
    return {"observed_bits": nbits, "matches": matches, "rate": rate}
