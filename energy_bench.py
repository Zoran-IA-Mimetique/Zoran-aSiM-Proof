# energy_bench.py (v25)
import time, json, random

def run_task():
    # simulate cpu/mem proxy values
    cpu = 20+random.random()*30
    mem = 40+random.random()*20
    time.sleep(0.1)
    return {"cpu_avg":cpu,"mem_avg":mem}

def main():
    logs=[]
    for i in range(10):
        logs.append(run_task())
    report={"meta":{"runs":10},"logs":logs}
    json.dump(report, open("ENERGY_BENCH_REPORT.json","w"), indent=2)
    print(json.dumps(report, indent=2))

if __name__=="__main__":
    main()
