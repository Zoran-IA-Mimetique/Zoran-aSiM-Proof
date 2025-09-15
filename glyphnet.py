
# glyphnet.py
import zlib, base64

HEADER = "Z5::"

def encode(text: str) -> str:
    raw = text.encode("utf-8")
    comp = zlib.compress(raw, level=9)
    b64 = base64.b64encode(comp).decode("ascii")
    return HEADER + b64

def decode(payload: str) -> str:
    assert payload.startswith(HEADER), "Invalid glyph header"
    b64 = payload[len(HEADER):]
    data = base64.b64decode(b64.encode("ascii"))
    return zlib.decompress(data).decode("utf-8")
