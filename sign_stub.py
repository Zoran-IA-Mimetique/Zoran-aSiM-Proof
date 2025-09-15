import sys, json, hashlib, time

def sha256(path):
    h = hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    if len(sys.argv)<2:
        print("Usage: python sign_stub.py <file_to_sign>")
        sys.exit(1)
    fpath = sys.argv[1]
    digest = sha256(fpath)
    stub = {"file": fpath, "sha256": digest, "signed_at": time.time(), "signer": "Zoran_stub"}
    out = fpath + ".sig.json"
    with open(out, "w") as f:
        json.dump(stub, f, indent=2)
    print(json.dumps({"written": out}, indent=2))

if __name__ == "__main__":
    main()
