# NODEGEN_EXPERIMENT.py (v42) — non-degeneration simulator
import json, random, math, time

SEEDS=[13,42,101]
PROMPTS=50

def whiteness_score(text):
    # toy: 1 - proportion subjective markers
    subjective = ["amazing","awesome","love","hate","terrible","brilliant","fantastic"]
    words = text.lower().split()
    hits = sum(1 for w in words if w in subjective)
    return max(0.0, 1.0 - hits/max(1,len(words)) * 5)

def style_vector(text):
    # toy style embedding: counts of headings/lists/caps
    h = text.count("#")
    l = text.count("- ")
    caps = sum(1 for c in text if c.isupper())
    return (h, l, caps)

def cos_sim(a,b):
    num = sum(x*y for x,y in zip(a,b))
    da = math.sqrt(sum(x*x for x in a))
    db = math.sqrt(sum(y*y for y in b))
    return num/(da*db) if da>0 and db>0 else 1.0

def gen_text(injected, length=120):
    base = "information " * (length//11)
    if injected:
        base = "# Title\n- item\n" + base + " AI Act evidence ERRATA"
    # add optional noise for baseline (more subjective)
    if not injected:
        base += " amazing fantastic"
    return base

def run_condition(injected: bool, seed: int):
    random.seed(seed)
    records=[]
    start = gen_text(injected, 200)
    start_vec = style_vector(start)
    for i in range(PROMPTS):
        txt = gen_text(injected, random.randint(100,220))
        w = whiteness_score(txt)
        vec = style_vector(txt)
        drift = 1.0 - cos_sim(start_vec, vec)
        records.append({"i":i,"whiteness":w,"drift":drift,"headings":vec[0],"lists":vec[1]})
    return records

def summarize(recs):
    def mean(xs): return sum(xs)/len(xs) if xs else 0.0
    w = [r["whiteness"] for r in recs]
    d = [r["drift"] for r in recs]
    c = [1 if r["headings"]>0 and r["lists"]>0 else 0 for r in recs]
    return {"whiteness_mean":mean(w),"drift_mean":mean(d),"consistency":mean(c)}

def main():
    out = {"meta":{"created": time.time()},"baseline":{},"injected":{}}
    for s in SEEDS:
        b = run_condition(False, s)
        inj = run_condition(True, s)
        out["baseline"][str(s)] = {"records":b,"summary":summarize(b)}
        out["injected"][str(s)] = {"records":inj,"summary":summarize(inj)}
    json.dump(out, open("NODEGEN_RESULTS.json","w"), indent=2)
    print("Wrote NODEGEN_RESULTS.json")
    # quick report
    rep = {"baseline":{}, "injected":{}}
    for k in out["baseline"]:
        rep["baseline"][k] = out["baseline"][k]["summary"]
        rep["injected"][k] = out["injected"][k]["summary"]
    json.dump(rep, open("NODEGEN_STATS.json","w"), indent=2)
    print(json.dumps(rep, indent=2))

if __name__=="__main__":
    main()
