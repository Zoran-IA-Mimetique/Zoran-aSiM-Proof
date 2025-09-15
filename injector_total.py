import os, json, time, hashlib, hmac, re
from datetime import datetime

VERSION = "v31"
FORBIDDEN = [r"\brm\s+-rf\b", r"\bimport\s+os\b", r"open\("]

def ascii_clean(s:str)->bool:
    # allow standard printable + newline/tab
    for ch in s:
        oc=ord(ch)
        if oc in (9,10,13): continue
        if oc<32 or oc>126:
            return False
    return True

def security_check(text:str):
    reasons=[]
    if not ascii_clean(text):
        reasons.append("non-ascii/control-char")
    for pat in FORBIDDEN:
        if re.search(pat, text, flags=re.IGNORECASE):
            reasons.append(f"forbidden:{pat}")
    return {"safe": len(reasons)==0, "reasons": reasons}

def hnorm(x): # 0..1 from hex string fragment
    return (int(x,16)%1000)/1000.0

def det_scores(context:str, content:str, role:str):
    # deterministic hash-based heuristics (no randomness)
    base = hashlib.sha256((context+"|"+content+"|"+role).encode("utf-8")).hexdigest()
    # derive four chunks
    q = hnorm(base[0:6])           # quality
    c = hnorm(base[6:12])          # coherence
    u = hnorm(base[12:18])         # utility
    o = 1.0 - hnorm(base[18:24])   # objectivity (invert)
    # Light boosts if obvious anchors present
    if role in ("compliance","report") and "AI Act" in content: u = min(1.0, u+0.15)
    if "#" in content or "-" in content: q = min(1.0, q+0.1)
    return {"quality": round(q,3), "coherence": round(c,3), "utility": round(u,3), "objectivity": round(o,3)}

def specialize(role:str, context:str, content:str, seed:int):
    # role-specific payload (deterministic via hashes)
    hx = hashlib.sha256((role+"|"+context+"|"+str(seed)).encode()).hexdigest()
    if role=="compliance":
        total = 8
        passed = (int(hx[:4],16) % (total+1))
        return {"compliance":{"items_total":total,"items_passed":passed,"score": round(passed/total,3)}}
    if role=="energy":
        cpu = (int(hx[4:8],16)%4000)/100.0  # 0..40
        mem = (int(hx[8:12],16)%5000)/100.0 # 0..50
        proxy = round(((cpu/100.0)+(mem/100.0))/2,3)
        return {"energy":{"cpu_avg":cpu,"mem_avg":mem,"proxy":proxy}}
    if role=="report":
        present=["metrics_humble_psutil.json","C2PA_manifest_full.json"]
        missing=["external_audit_report"]
        return {"report":{"present":present,"missing":missing,"summary_fr":"Pack HUMBLE: preuves présentes; audit externe à venir."}}
    if role=="audit":
        return {"audit":{"errata_candidates":["Overclaim risk"],"claims_mismatch":[] }}
    if role=="summary":
        return {"summary":{"imrad":["Intro","Methods","Results","Discussion"],"limits":["Simulations only"]}}
    if role=="bench":
        return {"bench":{"datasets":["sudoku_small"],"seeds":[13,42,101],"metrics":["success","length"],"ablations":["-ΔM11.3","-ZDM"]}}
    return {"custom":{"note":"no-op"}}

def decide(sec:dict, rel:dict, thresholds:dict):
    if not sec["safe"]:
        return {"accepted": False, "reasons": ["security_fail:"+",".join(sec["reasons"])]}
    fails=[]
    for k,thr in thresholds.items():
        if rel.get(k,0.0) < thr:
            fails.append(f"{k}<{thr}")
    if fails:
        return {"accepted": False, "reasons": fails}
    return {"accepted": True, "reasons": []}

def sign_payload(obj:dict)->str:
    key = os.environ.get("ZORAN_SIGN_KEY","zoran_demo_key").encode("utf-8")
    raw = json.dumps(obj, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hmac.new(key, raw, hashlib.sha256).hexdigest()

def run(context:str, content:str, role:str, seed:int=31, thresholds=None, out_name=None):
    thresholds = thresholds or {"quality":0.5,"coherence":0.5,"utility":0.5,"objectivity":0.5}
    meta={"created_iso": datetime.utcnow().isoformat()+"Z","seed":seed,"version":VERSION}
    sec = security_check(content)
    rel = det_scores(context, content, role)
    role_payload = specialize(role, context, content, seed)
    decision = decide(sec, rel, thresholds)
    log = {
        "meta": meta,
        "input": {"role":role, "context_len": len(context), "content_len": len(content)},
        "security": sec,
        "relevance": rel,
        "role": role_payload,
        "decision": decision
    }
    sig = sign_payload(log)
    log["signature"] = sig
    fname = out_name or f"injector_total_log_{seed}.json"
    with open(fname,"w",encoding="utf-8") as f:
        json.dump(log, f, indent=2, ensure_ascii=False)
    return log

if __name__=="__main__":
    # simple CLI demo
    import sys
    ctx = "HUMBLE ONLY context; AI Act mapping exists."
    txt = "This is a demo content with AI Act mention.\n# Section\n- item"
    role = "report"
    run(ctx, txt, role, seed=31)
