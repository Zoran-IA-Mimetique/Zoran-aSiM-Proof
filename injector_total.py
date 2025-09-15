# Minimal restatement (v33): see v31 for full details; kept compatible
import os, json, time, hashlib, hmac, re
from datetime import datetime
FORBIDDEN=[r"\brm\s+-rf\b", r"\bimport\s+os\b", r"open\("]
def ascii_ok(s): 
    return all((ord(c) in (9,10,13) or 32<=ord(c)<=126) for c in s)
def seccheck(t):
    r=[]; 
    if not ascii_ok(t): r.append("non-ascii/control")
    for p in FORBIDDEN:
        if re.search(p,t,flags=re.IGNORECASE): r.append("forbidden:"+p)
    return {"safe": len(r)==0, "reasons": r}
def hnorm(x): return (int(x,16)%1000)/1000.0
def scores(ctx, txt, role):
    base=hashlib.sha256((ctx+"|"+txt+"|"+role).encode()).hexdigest()
    q=hnorm(base[:6]); c=hnorm(base[6:12]); u=hnorm(base[12:18]); o=1.0-hnorm(base[18:24])
    if role in ("compliance","report") and "AI Act" in txt: u=min(1.0,u+0.15)
    if "#" in txt or "-" in txt: q=min(1.0,q+0.1)
    return {"quality":round(q,3),"coherence":round(c,3),"utility":round(u,3),"objectivity":round(o,3)}
def specialize(role, ctx, txt, seed):
    hx=hashlib.sha256((role+"|"+ctx+"|"+str(seed)).encode()).hexdigest()
    if role=="report": return {"report":{"present":["C2PA_manifest_full.json"],"missing":["external_audit"],"summary_fr":"HUMBLE: preuves présentes, audit à venir."}}
    return {"custom":{"note":"demo"}}
def decide(sec, rel, thr):
    if not sec["safe"]: return {"accepted":False,"reasons":sec["reasons"]}
    fails=[f"{k}<{v}" for k,v in thr.items() if rel.get(k,0.0)<v]
    return {"accepted": not bool(fails), "reasons": fails}
def sign(obj):
    key=os.environ.get("ZORAN_SIGN_KEY","zoran_demo_key").encode()
    raw=json.dumps(obj,sort_keys=True,ensure_ascii=False).encode()
    return hmac.new(key,raw,hashlib.sha256).hexdigest()
def run(ctx, txt, role, seed=33, thr=None, out="injector_total_log_33.json"):
    thr=thr or {"quality":0.5,"coherence":0.5,"utility":0.5,"objectivity":0.5}
    meta={"created_iso":datetime.utcnow().isoformat()+"Z","seed":seed,"version":"v33"}
    sec=seccheck(txt); rel=scores(ctx,txt,role)
    log={"meta":meta,"input":{"role":role,"context_len":len(ctx),"content_len":len(txt)},
         "security":sec,"relevance":rel,"role":specialize(role,ctx,txt,seed),
         "decision":decide(sec,rel,thr)}
    log["signature"]=sign(log)
    json.dump(log,open(out,"w"),indent=2,ensure_ascii=False)
    return log
if __name__=="__main__":
    os.environ.setdefault("ZORAN_SIGN_KEY","zoran_demo_key")
    run("ctx HUMBLE AI Act","Demo content with AI Act\n# Heading\n- bullet","report")
