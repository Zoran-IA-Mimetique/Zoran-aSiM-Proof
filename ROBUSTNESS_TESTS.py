# ROBUSTNESS_TESTS.py — mutations & detection rates
import json, random, re
from semantic_crypto_v37 import embed, detect

random.seed(37)
CLIENT_KEY="FranceTravail_demo_key"

def mutate(text):
    # Apply small mutations: case, punctuation, whitespace, random synonym swap outside pairs
    ops = []
    # lowercase 30%
    if random.random()<0.3: text=text.lower(); ops.append("lower")
    # punctuation sprinkle 30%
    if random.random()<0.3: text=re.sub(r"(\w)", r"\1,", text, count=5); ops.append("punct")
    # whitespace normalize 30%
    if random.random()<0.3: text=re.sub(r"\s+", " ", text); ops.append("ws")
    # light dropout 20%
    if random.random()<0.2: text=re.sub(r"\b\w{4}\b","", text, count=3); ops.append("drop4")
    return text, ops

def run():
    base = "We start this report to show how an idea can help small teams begin a big project. We try to use simple words and demonstrate the goal with a clear summary. If you need to get results fast, we assist you to make the right choices and finish on time."
    wm,_=embed(base, CLIENT_KEY)
    records=[]
    for i in range(50):
        t,ops = mutate(wm)
        ok=detect(t, CLIENT_KEY)
        wrong=detect(t, "wrong")
        records.append({"i":i,"ops":"+".join(ops),"correct_rate":ok["rate"],"wrong_rate":wrong["rate"]})
    # summary
    corr = [r["correct_rate"] for r in records]
    wrong = [r["wrong_rate"] for r in records]
    summary={"avg_correct": sum(corr)/len(corr), "avg_wrong": sum(wrong)/len(wrong)}
    out={"summary":summary,"records":records}
    json.dump(out, open("ROBUSTNESS_REPORT.json","w"), indent=2)
    # CSV
    import csv
    with open("ROBUSTNESS_REPORT.csv","w",newline="") as f:
        w=csv.writer(f); w.writerow(["i","ops","correct_rate","wrong_rate"])
        for r in records:
            w.writerow([r["i"], r["ops"], f"{r['correct_rate']:.3f}", f"{r['wrong_rate']:.3f}"])
    print(json.dumps(summary, indent=2))

if __name__=="__main__":
    run()
