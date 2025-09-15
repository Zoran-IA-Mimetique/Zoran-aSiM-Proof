import json, sys, hashlib, hmac, os
HMAC_KEY = os.environ.get('ZORAN_SIGN_KEY', 'zoran_demo_key')

def hmac_sha256_hex(key: bytes, payload: bytes) -> str:
    import hmac, hashlib
    return hmac.new(key, payload, hashlib.sha256).hexdigest()

def validate_signature(obj):
    sig = obj.get('signature')
    if sig is None: return False, 'missing overall signature'
    raw = json.dumps({k:v for k,v in obj.items() if k!='signature'}, sort_keys=True).encode('utf-8')
    expected = hmac_sha256_hex(HMAC_KEY.encode('utf-8'), raw)
    return expected==sig, ('ok' if expected==sig else f'bad_sig expected={expected} got={sig}')

def main(path):
    obj = json.load(open(path,'r', encoding='utf-8'))
    ok, reason = validate_signature(obj)
    print(json.dumps({'file':path,'valid_signature':ok,'reason':reason}, indent=2))
    # quick structural checks
    ok2 = isinstance(obj.get('provenance'), dict) and isinstance(obj.get('runs'), list)
    print(json.dumps({'structure_ok': ok2}, indent=2))

if __name__=='__main__':
    if len(sys.argv)<2:
        print('usage: validate_bifurcate.py <file>')
    else:
        main(sys.argv[1])
