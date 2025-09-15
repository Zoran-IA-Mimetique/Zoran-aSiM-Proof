# glyphnet_codec.py (v20) — lossless container
import base64, zlib

MAGIC = "Z5::"

def encode(text: str) -> dict:
    raw = text.encode("utf-8")
    comp = zlib.compress(raw, 9)
    b64 = base64.b64encode(comp).decode("ascii")
    return {"header": MAGIC, "b64": b64}

def decode(msg: dict) -> str:
    assert msg.get("header")==MAGIC, "Bad header"
    b64 = msg["b64"].encode("ascii")
    comp = base64.b64decode(b64)
    out = zlib.decompress(comp).decode("utf-8")
    return out

def encode_to_str(text: str) -> str:
    return MAGIC + base64.b64encode(zlib.compress(text.encode("utf-8"), 9)).decode("ascii")

def decode_from_str(payload: str) -> str:
    assert payload.startswith(MAGIC), "Bad header"
    b64 = payload[len(MAGIC):].encode("ascii")
    return zlib.decompress(base64.b64decode(b64)).decode("utf-8")
