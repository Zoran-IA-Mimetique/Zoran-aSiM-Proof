import zlib, base64, json, random, time
HEADER='Z5::'
def encode(text):
    c=zlib.compress(text.encode('utf-8'),9)
    return HEADER + base64.b64encode(c).decode('ascii')
def decode(payload):
    assert payload.startswith(HEADER)
    b=base64.b64decode(payload[len(HEADER):].encode('ascii'))
    return zlib.decompress(b).decode('utf-8')
def main():
    txt='The quick brown fox jumps over the lazy dog ' * 3
    enc=encode(txt)
    dec=decode(enc)
    ok = dec==txt
    out={'roundtrip_ok':ok,'orig_len':len(txt),'enc_len':len(enc)}
    with open('roundtrip_results.json','w') as f:
        json.dump(out,f,indent=2)
    print('Wrote roundtrip_results.json', out)
if __name__=='__main__': main()
