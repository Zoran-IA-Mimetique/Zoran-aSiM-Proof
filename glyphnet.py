
import zlib, base64
HEADER = "Z5::"
def encode(text: str) -> str:
    comp = zlib.compress(text.encode("utf-8"), 9)
    return HEADER + base64.b64encode(comp).decode("ascii")
def decode(payload: str) -> str:
    assert payload.startswith(HEADER)
    data = base64.b64decode(payload[len(HEADER):].encode("ascii"))
    return zlib.decompress(data).decode("utf-8")
