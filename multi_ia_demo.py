# multi_ia_demo.py (v21)
# Simulated HyperGlottal / QuantaGlottal injection across "agents" A and B.
import random, json, time
from hyperglottal_encoder import build as hg_build
from quantaglottal_encoder import tag as q_tag

def simulate_agent(name:str, message:str)->dict:
    # simple simulation: 90% chance of consistent parse, 10% random drift
    ok=random.random()>0.1
    return {"agent":name,"message":message,"understood":ok,"ts":time.time()}

def main():
    hyper=hg_build("auditor","check claims",["zero-claim","evidence-first"],"CLAIMS_AUDIT.md")
    quanta=q_tag("audit","zero-claim","CLAIMS_AUDIT.md")
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
