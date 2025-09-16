# make_audit_archive.py (v57)
import os, json, hashlib, zipfile, time
from pathlib import Path

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for ch in iter(lambda: f.read(8192), b""):
            h.update(ch)
    return h.hexdigest()

def main():
    files=[f for f in os.listdir(".") if f.startswith(("BASE_","INJ_","BENCH","ROOT_SHA")) and os.path.isfile(f)]
    manifest={"generated":time.time(),"files":[]}
    for f in files:
        manifest["files"].append({"name":f,"sha256":sha256(f),"bytes":os.path.getsize(f)})
    Path("AUDIT_SHA_MANIFEST.json").write_text(json.dumps(manifest,indent=2))
    zipname="AUDIT_ARCHIVE_v57.zip"
    with zipfile.ZipFile(zipname,"w",zipfile.ZIP_DEFLATED) as z:
        for f in files+["AUDIT_SHA_MANIFEST.json"]:
            z.write(f,arcname=f)
    print(f"Wrote {zipname} with {len(files)} files + manifest")

if __name__=="__main__":
    main()
