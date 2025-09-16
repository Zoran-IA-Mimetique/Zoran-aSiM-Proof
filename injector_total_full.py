# injector_total_full from v45 (short)
import os, re, json, hmac, hashlib
from datetime import datetime
FORBIDDEN=[r"\brm\s+-rf\b", r"\bimport\s+os\b", r"open\("]
SUBJ=re.compile(r"\b(amazing|awesome|terrible|fantastic|love|hate|great|awful)\b", re.I)
def ascii_ok(s): return all((ord(c) in (9,10,13) or 32<=ord(c)<=126) for c in s)
def seccheck(t):
    r=[]; 
    if not ascii_ok(t): r.append("non-ascii/control")
    for p in FORBIDDEN:
        if re.search(p,t,flags=re.IGNORECASE): r.append("forbidden:"+p)
    return {"safe": len(r)==0, "reasons": r}
def score_quality(t): return round(max(0.0,1.0-0.05*len(SUBJ.findall(t))),3)
def score_coherence(ctx,t):
    c=set(re.findall(r"\w+",ctx.lower())); x=set(re.findall(r"\w+",t.lower()))
    return round(len(c&x)/max(1,len(x)),3)
def score_utility(ctx,t):
    intents={"define":["definition","is","means"],"plan":["steps","roadmap","plan"],"compare":["vs","difference"],"audit":["evidence","manifest","sha"]}
    hits=0; tot=0
    for k,outs in intents.items():
        if k in ctx.lower():
            tot+=1
            if any(o in t.lower() for o in outs): hits+=1
    return round(hits/tot if tot>0 else min(1.0,len(t)/400),3)
def score_objectivity(t):
    refs=len(re.findall(r"(json|csv|sha|doi|http)",t.lower()))
    return round(min(1.0,0.6+0.1*refs),3)
def rel_scores(ctx,t): return {"quality":score_quality(t),"coherence":score_coherence(ctx,t),"utility":score_utility(ctx,t),"objectivity":score_objectivity(t)}
def decide(s,thr=None):
    thr=thr or {"quality":0.5,"coherence":0.5,"utility":0.5,"objectivity":0.5}
    fails=[k for k,v in thr.items() if s.get(k,0.0)<v]; return {"accepted":len(fails)==0,"fails":fails}
def sign(obj):
    key=os.environ.get("ZORAN_SIGN_KEY","zoran_demo_key").encode()
    raw=json.dumps(obj,sort_keys=True,ensure_ascii=False).encode()
    return hmac.new(key,raw,hashlib.sha256).hexdigest()
def run(ctx,t,role,seed=45,out="injector_total_full_log.json"):
    sec=seccheck(t); s=rel_scores(ctx,t); dec=decide(s); ok = sec["safe"] and dec["accepted"]
    log={"meta":{"created_iso":datetime.utcnow().isoformat()+"Z","seed":seed,"version":"v45"},
         "input":{"role":role,"context_len":len(ctx),"content_len":len(t)},"security":sec,"relevance":s,
         "decision":{"accepted":ok,"reasons":([] if ok else (sec['reasons']+dec['fails']))}}
    log["signature"]=sign(log); json.dump(log,open(out,"w"),indent=2,ensure_ascii=False); return log
if __name__=="__main__":
    os.environ.setdefault("ZORAN_SIGN_KEY","zoran_demo_key")
    run("define audit","Definition with checklist and sha manifest. # Title - item","report")
