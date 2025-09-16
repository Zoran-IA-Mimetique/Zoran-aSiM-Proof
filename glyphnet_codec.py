import base64,zlib
MAGIC="Z5::"
def encode(text:str)->str:
    return MAGIC+base64.b64encode(zlib.compress(text.encode('utf-8'),9)).decode('ascii')
def decode(payload:str)->str:
    assert payload.startswith(MAGIC)
    b=base64.b64decode(payload[len(MAGIC):].encode('ascii'))
    return zlib.decompress(b).decode('utf-8')
