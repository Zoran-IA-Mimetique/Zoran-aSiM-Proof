
import os, json, hashlib, datetime, sys

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def main(root="."):
    assets = []
    for dirpath, _, files in os.walk(root):
        # skip .git directory
        if ".git" in dirpath.split(os.sep):
            continue
        for fn in files:
            if fn.startswith("."): 
                continue
            p = os.path.join(dirpath, fn)
            rel = os.path.relpath(p, root).replace("\\","/")
            if rel.startswith(".github/"): 
                continue
            if rel.endswith(".pyc"): 
                continue
            assets.append({"name": rel, "sha256": sha256_file(p), "bytes": os.path.getsize(p)})
    manifest = {
        "c2pa":"v1",
        "created": datetime.datetime.utcnow().isoformat()+"Z",
        "creator": {"name":"Frédéric Tabary","org":"Zoran aSiM"},
        "license":"MIT",
        "assets": assets
    }
    with open("C2PA_manifest_full.json","w") as f:
        json.dump(manifest, f, indent=2)
    print("C2PA manifest updated with", len(assets), "assets.")

if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv)>1 else "."
    main(root)
