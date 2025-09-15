import os, hashlib, json, datetime, sys
def sha256(fpath):
    h=hashlib.sha256()
    with open(fpath,"rb") as fh:
        for chunk in iter(lambda: fh.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()
root = sys.argv[1] if len(sys.argv)>1 else '.'
assets=[]
for dirpath, _, files in os.walk(root):
    if '.git' in dirpath.split(os.sep): continue
    for fn in files:
        if fn.startswith('.'): continue
        p=os.path.join(dirpath,fn)
        rel=os.path.relpath(p,root).replace('\\','/')
        assets.append({'name':rel,'sha256':sha256(p),'bytes':os.path.getsize(p)})
manifest={'c2pa':'v1','created':datetime.datetime.utcnow().isoformat()+'Z','creator':{'name':'Frédéric Tabary','org':'Zoran aSiM'},'assets':assets}
with open('C2PA_manifest_full.json','w') as f: json.dump(manifest,f,indent=2)
print('C2PA manifest written with',len(assets),'assets')
