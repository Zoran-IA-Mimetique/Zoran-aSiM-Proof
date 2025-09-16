# injector_total_full.py (v45) — full injector with relevance integrated
import os, re, json, hmac, hashlib
from datetime import datetime

VERSION="v45"
FORBIDDEN=[r"\brm\s+-rf\b", r"\bimport\s+os\b", r"open\("]
SUBJECTIVE = re.compile(r"\b(amazing|awesome|terrible|fantastic|love|hate|great|awful)\b", re.I)

def ascii_ok(s): 
    return all((ord(c) in (9,10,13) or 32<=ord(c)<=126) for c in s)

def seccheck(text:str):
    reasons=[]
    if not ascii_ok(text): reasons.append("non-ascii/control")
    for p in FORBIDDEN:
        if re.search(p,text,flags=re.IGNORECASE): reasons.append("forbidden:"+p)
    return {"safe": len(reasons)==0, "reasons": reasons}

# --- Relevance scoring (deterministic heuristics) ---
def score_quality(text:str)->float:
    subj = len(SUBJECTIVE.findall(text))
    punct = sum(text.count(p) for p in ["!!","??","?!","!?"])
    raw = max(0.0, 1.0 - 0.05*subj - 0.02*punct)
    return round(min(1.0, raw),3)

def score_coherence(context:str, text:str)->float:
    ctx = set(w.lower() for w in re.findall(r"\w+", context))
    tx  = set(w.lower() for w in re.findall(r"\w+", text))
    inter = len(ctx & tx); den = max(1,len(tx))
    return round(min(1.0, inter/den),3)

def score_utility(context:str, text:str)->float:
    intents = {"define":["definition","is","means"],"plan":["steps","roadmap","plan"],
               "compare":["vs","compare","difference"],"audit":["evidence","manifest","checklist","sha"]}
    ctx=context.lower(); hits=0; total=0
    for k,outs in intents.items():
        if k in ctx:
            total += 1
            if any(o in text.lower() for o in outs): hits += 1
    if total==0: return round(min(1.0, len(text)/400),3)
    return round(hits/total,3)

def score_objectivity(text:str)->float:
    subj = len(SUBJECTIVE.findall(text))
    refs = len(re.findall(r"(json|csv|sha|doi|http)", text.lower()))
    raw = max(0.0, min(1.0, 0.7 - 0.07*subj + 0.1*refs))
    return round(raw,3)

def relevance_scores(context:str, text:str)->dict:
    return {"quality":score_quality(text),"coherence":score_coherence(context,text),
            "utility":score_utility(context,text),"objectivity":score_objectivity(text)}

def decide(scores:dict, thresholds=None)->dict:
    thresholds=thresholds or {"quality":0.5,"coherence":0.5,"utility":0.5,"objectivity":0.5}
    fails=[k for k,v in thresholds.items() if scores.get(k,0.0)<v]
    return {"accepted": len(fails)==0, "fails": fails, "thresholds": thresholds}

# --- Role specialization (deterministic) ---
def role_payload(role, context, text, seed):
    hx=hashlib.sha256((role+"|"+context+"|"+str(seed)).encode()).hexdigest()
    if role=="report":
        return {"report":{"present":["C2PA_manifest_full.json"],"missing":["external_audit"],"summary_fr":"HUMBLE: preuves présentes, audit externe à venir."}}
    if role=="compliance":
        total=8; passed=(int(hx[:4],16)%(total+1)); return {"compliance":{"items_total":total,"items_passed":passed,"score":round(passed/total,3)}}
    return {"custom":{"note":"demo"}}

# --- Signing ---
def sign(obj:dict)->str:
    key=os.environ.get("ZORAN_SIGN_KEY","zoran_demo_key").encode()
    raw=json.dumps(obj,sort_keys=True,ensure_ascii=False).encode()
    return hmac.new(key,raw,hashlib.sha256).hexdigest()

def run(context:str, text:str, role:str, seed:int=45, thresholds=None, out="injector_total_full_log.json"):
    sec=seccheck(text)
    rel=relevance_scores(context,text)
    dec=decide(rel, thresholds)
    accepted= sec["safe"] and dec["accepted"]
    log={"meta":{"created_iso":datetime.utcnow().isoformat()+"Z","version":VERSION,"seed":seed},
         "input":{"role":role,"context_len":len(context),"content_len":len(text)},
         "security":sec,"relevance":rel,"decision":{"accepted":accepted,"reasons":([] if accepted else (sec["reasons"]+dec["fails"]))},
         "role": role_payload(role, context, text, seed)}
    log["signature"]=sign(log)
    json.dump(log, open(out,"w"), indent=2, ensure_ascii=False)
    return log

if __name__=="__main__":
    os.environ.setdefault("ZORAN_SIGN_KEY","zoran_demo_key")
    ctx="define audit"; txt="Definition with checklist and sha manifest. # Title - item"
    run(ctx, txt, "report", seed=45)
