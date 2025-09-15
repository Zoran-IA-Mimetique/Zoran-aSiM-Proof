# run_dataset_bench.py — integrate sudoku + maze datasets (toy benchmark)
import json,time,random
from sudoku_loader import gen_sudoku
from maze_loader import gen_dataset

def run_bench(out="dataset_bench_results.json"):
    sud=gen_sudoku(3,seed=13)
    mazes=gen_dataset(3,w=8,h=8,seed=42)
    results=[]
    # simulate scoring
    for p in sud:
        score=random.uniform(0.5,0.9)
        results.append({"type":"sudoku","id":p["id"],"score":score})
    for m in mazes:
        score=random.uniform(0.6,0.95)
        results.append({"type":"maze","id":m["id"],"score":score})
    data={"meta":{"created":time.time()},"results":results}
    with open(out,"w") as f: json.dump(data,f,indent=2)
    print("Wrote",out)
    return out

if __name__=="__main__":
    run_bench()
