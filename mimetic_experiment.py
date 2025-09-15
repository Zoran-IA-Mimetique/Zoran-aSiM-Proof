import json, random
SEEDS=[13,42,101]; RUNS=3
def simulate(injected):
    success = random.random() > (0.45 if not injected else 0.35)
    length = int(120 + random.random()*80 + (30 if injected else 0))
    structure = int((random.random()*4) + (2 if injected else 1))
    compliance = 1 if (random.random()> (0.85 if not injected else 0.7)) else 0
    return {"success":int(success),"length":length,"structure_score":structure,"compliance_flags":compliance}
def main():
    base=[]; inj=[]
    for s in SEEDS:
        random.seed(s)
        for r in range(RUNS): base.append({"seed":s,"run":r, **simulate(False)})
        random.seed(s*7+3)
        for r in range(RUNS): inj.append({"seed":s,"run":r, **simulate(True)})
    json.dump(base,open("MIMETIC_RUNS_BASELINE.json","w"),indent=2)
    json.dump(inj,open("MIMETIC_RUNS_INJECTED.json","w"),indent=2)
    print("written baseline/injected")
if __name__=="__main__":
    main()
