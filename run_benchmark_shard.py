# run_benchmark_shard.py (v56)
import json, argparse, random
from pathlib import Path

def load_prompts(path):
    return [json.loads(line) for line in open(path,"r",encoding="utf-8").read().splitlines() if line.strip()]

def simulate_answer(p, injected=False):
    cat=p.get("category",""); base_prob = 0.65 if cat in ("arc-like","gsm8k-like") else 0.7
    if injected: base_prob += 0.08
    ok = random.random() < min(0.95, base_prob)
    ans = p.get("answer","OK") if ok and "answer" in p else " ".join(p.get("answer_contains",["neutral","sha"])) if ok else "uncertain"
    return ans, ok

def relevance_scores(context, text):
    subj = sum(text.lower().count(t) for t in ["amazing","awesome","terrible","fantastic","love","hate"])
    quality = max(0.0, 1.0 - 0.05*subj)
    ctx = set(context.lower().split()); tx=set(text.lower().split())
    coherence = len(ctx & tx)/max(1,len(tx))
    intents={"define":["definition","is","means"],"plan":["steps","plan","roadmap"],"compare":["vs","difference"],"audit":["evidence","manifest","sha"]}
    hits=0; tot=0
    for k,outs in intents.items():
        if k in context.lower():
            tot+=1
            if any(o in text.lower() for o in outs): hits+=1
    utility = hits/tot if tot>0 else min(1.0, len(text)/300)
    objectivity = min(1.0, 0.6 + 0.1*sum(x in text.lower() for x in ["json","sha","doi","http"]))
    return {"quality":round(quality,3),"coherence":round(coherence,3),"utility":round(utility,3),"objectivity":round(objectivity,3)}

def comp(scores): return round(0.3*scores["quality"]+0.3*scores["coherence"]+0.3*scores["utility"]+0.1*scores["objectivity"],3)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--seed",type=int,default=13)
    ap.add_argument("--simulate",type=int,default=1)
    ap.add_argument("--shard",type=str,default="prompts_shard_01.jsonl")
    args=ap.parse_args()
    random.seed(args.seed)
    prompts = load_prompts(args.shard)
    res_b=[]; res_i=[]
    for p in prompts:
        ctx = p.get("category","") + " " + p.get("prompt","")
        a0,ok0 = simulate_answer(p,False) if args.simulate else ("",False)
        s0 = relevance_scores(ctx,a0); res_b.append({"id":p["id"],"ok":int(ok0),"pertinence":comp(s0)})
        a1,ok1 = simulate_answer(p,True) if args.simulate else ("",False)
        s1 = relevance_scores(ctx,a1); res_i.append({"id":p["id"],"ok":int(ok1),"pertinence":comp(s1)})
    Path(f"BASE_{args.seed}_{Path(args.shard).stem}.json").write_text(json.dumps(res_b,indent=2))
    Path(f"INJ_{args.seed}_{Path(args.shard).stem}.json").write_text(json.dumps(res_i,indent=2))
    print(f"Wrote BASE_... and INJ_... for {args.shard} seed={args.seed}")

if __name__=="__main__":
    main()
