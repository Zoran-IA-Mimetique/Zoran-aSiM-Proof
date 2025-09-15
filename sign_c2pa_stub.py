
"""sign_c2pa_stub.py
Generate a simple C2PA-like manifest JSON for a set of files, signing the manifest with KMS/HMAC.
Usage:
  python tools/sign_c2pa_stub.py <file1> <file2> ...
Env:
  SIGN_MODE, AWS_KMS_KEY_ID, AWS_REGION, ZORAN_SIGN_KEY (hmac fallback)
Output: c2pa_signed_manifest.json
"""
import sys, os, json, hashlib, time
from tools.sign_kms_wrapper import sign_bytes

def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for ch in iter(lambda: f.read(8192), b''):
            h.update(ch)
    return h.hexdigest()

def build_manifest(files):
    entries = []
    for f in files:
        if os.path.isfile(f):
            entries.append({'name': f, 'sha256': sha256(f)})
    manifest = {'created': time.time(), 'creator':'Zoran_pack', 'assets': entries}
    return manifest

if __name__=='__main__':
    files = sys.argv[1:]
    manifest = build_manifest(files)
    raw = json.dumps(manifest, sort_keys=True).encode('utf-8')
    sig = sign_bytes(raw)
    out = {'manifest': manifest, 'signature': sig}
    with open('c2pa_signed_manifest.json','w') as f:
        json.dump(out, f, indent=2)
    print('wrote c2pa_signed_manifest.json')
