import random, json, time
def simulate_agent(name:str, message:str)->dict:
    ok = random.random()>0.1
    return {"agent":name,"message":message,"understood":ok,"ts":time.time()}
def main():
    hyper = "#HG v20\nROLE: auditor\nTASK: check claims\nPOLICY: zero-claim,evidence-first\nEVIDENCE: CLAIMS_AUDIT.md\nEND"
    quanta = "⟦chan:role=audit|policy=zero-claim|evidence=CLAIMS_AUDIT.md⟧"
    agents=["A","B","C"]
    logs=[]
    for a in agents:
        logs.append(simulate_agent(a,hyper))
        logs.append(simulate_agent(a,quanta))
    report={"meta":{"created":time.time(),"agents":agents},"logs":logs}
    json.dump(report,open("MULTI_IA_DEMO_LOG.json","w"),indent=2)
    print(json.dumps(report,indent=2))
if __name__=="__main__":
    main()
