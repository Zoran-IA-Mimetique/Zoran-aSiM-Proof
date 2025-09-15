# semantic_demo.py (v36) — end-to-end demo
import os, json, subprocess, time, hashlib
def sha(p):
    import hashlib
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for ch in iter(lambda: f.read(8192), b""):
            h.update(ch)
    return h.hexdigest()
def main():
    os.environ.setdefault("ZORAN_CLIENT_KEY","FranceTravail_demo_key")
    # run verification
    subprocess.run(["python","verify_semantic_crypto.py"], check=False)
    # collect proofs
    proofs = {}
    for f in ["sample_text.txt","sample_text_zoranX.txt","verification_report.json"]:
        if os.path.isfile(f):
            proofs[f] = {"sha256": sha(f), "bytes": os.path.getsize(f)}
    json.dump({"generated": time.time(), "proofs": proofs}, open("semantic_demo_log.json","w"), indent=2)
    print(json.dumps({"proofs": proofs}, indent=2))
if __name__=="__main__":
    main()
