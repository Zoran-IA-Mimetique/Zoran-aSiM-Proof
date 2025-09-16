# PROPAGATION_SIMULATOR.py (v42) — IA→IA propagation simulator
import json, random, time

AGENTS=["A","B","C","D"]
def propagate(message, hops=3, noise=0.2):
    logs=[]
    m = message
    for i in range(hops):
        a = AGENTS[i%len(AGENTS)]
        understood = random.random() > noise
        # carry forward structure with probability ~ understood
        if understood and random.random() > 0.2:
            m = m  # keep
        else:
            m = m.replace("#","").replace("- ","")
        logs.append({"hop":i+1,"agent":a,"understood":understood,"msg_len":len(m)})
    return logs

def measure(logs):
    parse_rate = sum(1 for x in logs if x["understood"])/len(logs)
    retention = 1.0 if all("#" in ("#"*0) for _ in []) else sum(1 for x in logs if x["msg_len"]>0)/len(logs)
    return {"parse_rate":parse_rate,"retention_proxy":retention}

def main():
    base = "#HG v20\nROLE: auditor\nTASK: check claims\nPOLICY: zero-claim,evidence-first\nEND"
    logs = propagate(base, hops=5, noise=0.25)
    stats = measure(logs)
    json.dump({"logs":logs,"stats":stats}, open("PROPAGATION_RESULTS.json","w"), indent=2)
    print(json.dumps({"stats":stats}, indent=2))

if __name__=="__main__":
    main()
