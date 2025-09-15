import json, hashlib, os, argparse, time

MANIFEST_FILE = "AUDIT_READY_MANIFEST.json"
STRICT_SCHEMA = "injector_bifurcate_schema_strict.json"
STRICT_OUTPUT_GLOB = ["bifurcate_strict_16.json","bifurcate_strict_*.json"]

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for ch in iter(lambda: f.read(8192), b""):
            h.update(ch)
    return h.hexdigest()

def check_sha():
    if not os.path.isfile(MANIFEST_FILE):
        return {"error":"manifest_missing"}
    data = json.load(open(MANIFEST_FILE,"r"))
    files = data.get("files",[])
    ok, mismatch, missing = 0, [], []
    for e in files:
        name, expected = e["name"], e["sha256"]
        if not os.path.isfile(name):
            missing.append(name); continue
        actual = sha256(name)
        if actual == expected: ok += 1
        else: mismatch.append({"name":name,"expected":expected,"actual":actual})
    return {"checked": len(files), "ok": ok, "missing": missing, "mismatch": mismatch}

def check_strict():
    # optional strict checks without external libs
    report = {"schema_present": os.path.isfile(STRICT_SCHEMA), "files_checked": [], "notes": "Light check only (no jsonschema here)."}
    # verify presence/signature field existence
    import glob
    for pat in STRICT_OUTPUT_GLOB:
        for f in glob.glob(pat):
            obj = json.load(open(f,"r",encoding="utf-8"))
            report["files_checked"].append(f)
            # minimal structural assertions
            if not isinstance(obj.get("provenance"), dict): return {"error":"no_provenance","file":f}
            if not isinstance(obj.get("runs"), list): return {"error":"no_runs","file":f}
            if "signature" not in obj: return {"error":"no_signature","file":f}
    return report

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-sha", action="store_true")
    ap.add_argument("--check-strict", action="store_true")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    out = {"generated": time.time()}
    if args.check_sha or args.all:
        out["sha"] = check_sha()
    if args.check_strict or args.all:
        out["strict"] = check_strict()
    json.dump(out, open("SELF_CHECK_FINAL_REPORT.json","w"), indent=2)
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
