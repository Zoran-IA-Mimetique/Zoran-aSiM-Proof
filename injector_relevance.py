# injector_relevance.py (v44) — deterministic relevance scoring
import re, hashlib, json

SUBJECTIVE = re.compile(r"\b(amazing|awesome|terrible|fantastic|love|hate|great|awful)\b", re.I)

def score_quality(text:str)->float:
    # toy: penalize excessive punctuation / subjective words
    subj = len(SUBJECTIVE.findall(text))
    punct = sum(text.count(p) for p in [ "!!","??","?!","!?"])
    raw = max(0.0, 1.0 - 0.05*subj - 0.02*punct)
    return round(min(1.0, raw),3)

def score_coherence(context:str, text:str)->float:
    # toy: overlap of keywords (deterministic proxy)
    ctx = set(w.lower() for w in re.findall(r"\w+", context))
    tx  = set(w.lower() for w in re.findall(r"\w+", text))
    inter = len(ctx & tx); den = max(1,len(tx))
    return round(min(1.0, inter/den),3)

def score_utility(context:str, text:str)->float:
    # toy: look for intent keywords in context and corresponding patterns in text
    intents = {
        "define": ["definition","is","means"],
        "plan": ["steps","roadmap","plan"],
        "compare": ["vs","compare","difference"],
        "audit": ["evidence","manifest","checklist","sha"]
    }
    ctx = context.lower()
    hits = 0; total = 0
    for k,outs in intents.items():
        if k in ctx:
            total += 1
            if any(o in text.lower() for o in outs): hits += 1
    if total==0:
        # fallback: length heuristic
        return round(min(1.0, len(text)/400),3)
    return round(hits/total,3)

def score_objectivity(text:str)->float:
    # toy: penalize subjective markers; reward citations/figures-like tokens
    subj = len(SUBJECTIVE.findall(text))
    refs = len(re.findall(r"(json|csv|sha|doi|http)", text.lower()))
    raw = max(0.0, min(1.0, 0.7 - 0.07*subj + 0.1*refs))
    return round(raw,3)

def relevance_scores(context:str, text:str)->dict:
    return {
        "quality":     score_quality(text),
        "coherence":   score_coherence(context, text),
        "utility":     score_utility(context, text),
        "objectivity": score_objectivity(text)
    }

def decide(scores:dict, thresholds=None)->dict:
    thresholds = thresholds or {"quality":0.5,"coherence":0.5,"utility":0.5,"objectivity":0.5}
    fails = [k for k,v in thresholds.items() if scores.get(k,0.0) < v]
    return {"accepted": len(fails)==0, "fails": fails, "thresholds": thresholds}

if __name__=="__main__":
    import sys
    ctx = sys.argv[1] if len(sys.argv)>1 else "define audit"
    txt = sys.argv[2] if len(sys.argv)>2 else "This is a definition with a checklist and a SHA manifest."
    s = relevance_scores(ctx, txt)
    print(json.dumps({"scores":s,"decision": decide(s)}, indent=2))
