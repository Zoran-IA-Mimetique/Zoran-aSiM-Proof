
import json, os, glob, hashlib, sys, time
MANIFEST_GLOBS = ["ROOT_SHA256_MANIFEST_v*.json","ROOT_SHA256_MANIFEST.json"]

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def load_latest_manifest():
    files = []
    for g in MANIFEST_GLOBS:
        files += glob.glob(g)
    if not files:
        return None, None
    # pick the lexicographically last (vXX higher) or last modified
    files.sort()
    chosen = files[-1]
    try:
        data = json.load(open(chosen, "r"))
    except Exception:
        # if file is just a list of file entries, wrap it
        data = {"files": json.load(open(chosen, "r"))}
    return chosen, data

def main():
    chosen, data = load_latest_manifest()
    report = {"meta":{"time": time.time(), "manifest": chosen}, "mismatch": [], "missing": [], "ok": 0, "total": 0}
    if not chosen:
        report["error"] = "No ROOT_SHA256_MANIFEST found"
        json.dump(report, open("tools/sha_verify_report.json","w"), indent=2)
        print(json.dumps(report, indent=2))
        # no manifest == no check
        sys.exit(0)

    entries = data.get("files", [])
    for entry in entries:
        name = entry.get("name")
        expected = entry.get("sha256")
        if not name or not expected:
            continue
        report["total"] += 1
        if not os.path.isfile(name):
            report["missing"].append(name)
            continue
        actual = sha256(name)
        if actual != expected:
            report["mismatch"].append({"name": name, "expected": expected, "actual": actual})
        else:
            report["ok"] += 1

    json.dump(report, open("tools/sha_verify_report.json","w"), indent=2)
    print(json.dumps(report, indent=2))
    # Fail CI if any mismatch
    if report["mismatch"] or report["missing"]:
        sys.exit(1)

if __name__ == "__main__":
    main()
