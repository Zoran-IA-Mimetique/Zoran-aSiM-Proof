
"""tools/generate_release.py
Recompute ROOT SHA manifest, optionally sign with KMS/HMAC, and create a release zip.
Usage:
  python tools/generate_release.py --zipname release_vX.zip file1 file2 ...
Env:
  SIGN_MODE, AWS_KMS_KEY_ID, AWS_REGION, ZORAN_SIGN_KEY
"""
import sys, json, hashlib, time, os, zipfile
from tools.sign_kms_wrapper import sign_bytes

def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for ch in iter(lambda: f.read(8192), b''):
            h.update(ch)
    return h.hexdigest()

def build_manifest(files):
    entries=[]
    for f in files:
        if os.path.isfile(f):
            entries.append({'name': os.path.basename(f), 'sha256': sha256(f)})
    return {'created': time.time(), 'files': entries}

if __name__=='__main__':
    if len(sys.argv) < 3:
        print('usage: python tools/generate_release.py <zipname> <file1> [file2 ...]')
        sys.exit(1)
    zipname = sys.argv[1]
    files = sys.argv[2:]
    manifest = build_manifest(files)
    raw = json.dumps(manifest, sort_keys=True).encode('utf-8')
    sig = sign_bytes(raw)
    out_manifest = {'manifest': manifest, 'signature': sig}
    with open('release_manifest.json','w') as f:
        json.dump(out_manifest, f, indent=2)
    with zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in files:
            z.write(f, arcname=os.path.basename(f))
        z.write('release_manifest.json')
    print('created', zipname)
