# verify_semantic_crypto.py (v36)
import json, os, time, hashlib, hmac
from semantic_crypto import embed, detect

DEMO_KEY = os.environ.get("ZORAN_CLIENT_KEY","FranceTravail_demo_key")

def h(s): return hashlib.sha256(s.encode('utf-8')).hexdigest()

def main():
    base_text = open("sample_text.txt","r",encoding="utf-8").read()
    t0=time.time()
    watermarked, stats = embed(base_text, DEMO_KEY)
    t1=time.time()
    open("sample_text_zoranX.txt","w",encoding="utf-8").write(watermarked)
    detect_ok = detect(watermarked, DEMO_KEY)
    detect_wrong = detect(watermarked, "wrong_key_example")
    report = {
        "meta":{"created": time.time(),"algo":"lexical-watermark","pairs":"builtin"},
        "inputs":{"base_len": len(base_text), "key_hash": h(DEMO_KEY)},
        "embed":{"applied": stats["applied"], "candidates": stats["candidates"], "ms": (t1-t0)*1000},
        "detect_correct":{"observed_bits": detect_ok["observed_bits"], "matches": detect_ok["matches"], "rate": detect_ok["rate"]},
        "detect_wrong":{"observed_bits": detect_wrong["observed_bits"], "matches": detect_wrong["matches"], "rate": detect_wrong["rate"]}
    }
    json.dump(report, open("verification_report.json","w"), indent=2)
    print(json.dumps(report, indent=2))

if __name__=="__main__":
    # write log
    main()
