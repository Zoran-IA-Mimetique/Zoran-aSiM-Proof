# mimetic_experiment.py (v24)
# Simulated experiment runner that generates baseline vs injected outcomes with seeds.
import json, random, time
SEEDS=[13,42,101]
RUNS=3

def simulate_trial(injected: bool):
    random_val = random.random()
    success = random_val > (0.35 if injected else 0.45)  # injected slightly better
    length = int(120 + random.random()*80 + (30 if injected else 0))
    structure = int( (random.random()*4) + (2 if injected else 1) )  # headings/lists count rough proxy
    compliance = int(random.random()>0.7) if injected else int(random.random()>0.85)
    return {"success": int(success), "length": length, "structure_score": structure, "compliance_flags": compliance}

def run_all():
    baseline=[]; injected=[]
    for s in SEEDS:
        random.seed(s)
        for r in range(RUNS):
            baseline.append({"seed":s,"run":r, **simulate_trial(False)})
        random.seed(s*7+3)
        for r in range(RUNS):
            injected.append({"seed":s,"run":r, **simulate_trial(True)})
    json.dump(baseline, open("MIMETIC_RUNS_BASELINE.json","w"), indent=2)
    json.dump(injected, open("MIMETIC_RUNS_INJECTED.json","w"), indent=2)
    print("written MIMETIC_RUNS_BASELINE.json, MIMETIC_RUNS_INJECTED.json")

if __name__=="__main__":
    run_all()
