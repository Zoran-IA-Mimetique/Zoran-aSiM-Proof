import re, json
SUBJ=re.compile(r"\b(amazing|awesome|terrible|fantastic|love|hate|great|awful)\b", re.I)
def score_quality(t): return round(max(0.0,1.0-0.05*len(SUBJ.findall(t))),3)
def score_coherence(ctx,t):
    c=set(re.findall(r"\w+",ctx.lower())); x=set(re.findall(r"\w+",t.lower()))
    return round(len(c&x)/max(1,len(x)),3)
def score_utility(ctx,t):
    intents={"define":["definition","is","means"],"plan":["steps","plan","roadmap"],"compare":["vs","difference"],"audit":["evidence","manifest","sha"]}
    hits=0; tot=0
    for k,outs in intents.items():
        if k in ctx.lower():
            tot+=1
            if any(o in t.lower() for o in outs): hits+=1
    return round(hits/tot if tot>0 else min(1.0,len(t)/400),3)
def score_objectivity(t):
    refs=len(re.findall(r"(json|csv|sha|doi|http)",t.lower()))
    return round(min(1.0,0.6+0.1*refs),3)
def relevance_scores(ctx,t): return {"quality":score_quality(t),"coherence":score_coherence(ctx,t),"utility":score_utility(ctx,t),"objectivity":score_objectivity(t)}
def decide(scores,thr=None):
    thr=thr or {"quality":0.5,"coherence":0.5,"utility":0.5,"objectivity":0.5}
    fails=[k for k,v in thr.items() if scores.get(k,0.0)<v]; return {"accepted": len(fails)==0,"fails":fails,"thresholds":thr}
if __name__=="__main__":
    import sys
    ctx=sys.argv[1] if len(sys.argv)>1 else "define audit"
    txt=sys.argv[2] if len(sys.argv)>2 else "definition with checklist sha"
    s=relevance_scores(ctx,txt); print(json.dumps({"scores":s,"decision":decide(s)},indent=2))
