import json, os, subprocess, hashlib, sys

def sha256(p):
    import hashlib
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for ch in iter(lambda: f.read(8192), b""):
            h.update(ch)
    return h.hexdigest()

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=60)

def main():
    # Determinism test
    os.environ['ZORAN_SIGN_KEY'] = 'zoran_demo_key'
    run(["python","injector_bifurcate_strict.py","compliance,energy,report","strict_demo_ctx","16"])
    a = "bifurcate_strict_16.json"; ha = sha256(a)
    run(["python","injector_bifurcate_strict.py","compliance,energy,report","strict_demo_ctx","16"])
    b = "bifurcate_strict_16.json"; hb = sha256(b)
    det_ok = (ha==hb)

    # Schema validation
    v = run(["python","validate_bifurcate_strict.py",a])
    schema_ok = v.returncode==0

    # Tamper detection
    data = json.load(open(a,"r",encoding="utf-8"))
    data["runs"][0]["payload"]["values"]["ai_act_items_total"] = 999  # tamper
    tampered = "bifurcate_strict_16_tampered.json"
    json.dump(data, open(tampered,"w",encoding="utf-8"), indent=2)
    # simple signature validation (recompute expected & compare)
    import hmac, hashlib
    def recompute(obj):
        raw = json.dumps({k:v for k,v in obj.items() if k!='signature'}, sort_keys=True).encode('utf-8')
        return hmac.new(b'zoran_demo_key', raw, hashlib.sha256).hexdigest()
    sig_ok = (recompute(json.load(open(a))) == json.load(open(a))["signature"])
    sig_fail_on_tamper = (recompute(json.load(open(tampered))) != json.load(open(tampered))["signature"])

    report = {
        "determinism_sha_equal": det_ok,
        "schema_valid": schema_ok,
        "signature_valid_original": sig_ok,
        "signature_detects_tamper": sig_fail_on_tamper
    }
    json.dump(report, open("STRICT_TEST_REPORT.json","w"), indent=2)
    print(json.dumps(report, indent=2))

if __name__=="__main__":
    main()
