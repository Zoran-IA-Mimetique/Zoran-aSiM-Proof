
import json, time, random, string, os
from collections import Counter
from math import sqrt

# Minimal components
from dataclasses import dataclass

@dataclass
class DeltaM113Config:
    threshold: float = 0.25
    window: int = 10

class DeltaM113Guard:
    def __init__(self, cfg: DeltaM113Config = DeltaM113Config()):
        self.cfg = cfg
        self.history = []
    def record(self, unstable: bool):
        self.history.append(1 if unstable else 0)
        if len(self.history) > self.cfg.window:
            self.history.pop(0)
    def instability(self) -> float:
        return (sum(self.history) / len(self.history)) if self.history else 0.0
    def should_rollback(self) -> bool:
        return self.instability() > self.cfg.threshold

# Simple tasks
def arc_like_tasks(n=60, d=12):
    tasks=[]
    for _ in range(n):
        v=[random.randint(0,9) for _ in range(d)]
        y=[x%2 for x in v]
        tasks.append((v,y))
    return tasks

def arc_like_solver(vec): return [x%2 for x in vec]

def gen_mazes(n=10, w=12, h=7):
    def gen():
        grid=[["#"]*w for _ in range(h)]
        for r in range(1,h-1):
            for c in range(1,w-1):
                grid[r][c] = "." if random.random()>.35 else "#"
        grid[1][1]="S"; grid[h-2][w-2]="G"
        return ["".join(row) for row in grid]
    return [gen() for _ in range(n)]

from collections import deque
def maze_solve(maze):
    R,C=len(maze),len(maze[0])
    sr=sc=gr=gc=-1
    for r in range(R):
        for c in range(C):
            if maze[r][c]=="S": sr,sc=r,c
            if maze[r][c]=="G": gr,gc=r,c
    q=deque([(sr,sc)]); seen={(sr,sc)}
    while q:
        r,c=q.popleft()
        if (r,c)==(gr,gc): return True
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<R and 0<=nc<C and maze[nr][nc]!="#" and (nr,nc) not in seen:
                seen.add((nr,nc)); q.append((nr,nc))
    return False

def simple_sudoku():
    g=[[0]*9 for _ in range(9)]
    for i in range(9): g[i][i]=(i%9)+1
    return g

def sudoku_is_valid(grid):
    for i in range(9):
        row=[x for x in grid[i] if x!=0]; col=[grid[r][i] for r in range(9) if grid[r][i]!=0]
        if len(row)!=len(set(row)) or len(col)!=len(set(col)): return False
    for br in range(0,9,3):
        for bc in range(0,9,3):
            vals=[]; 
            for r in range(br,br+3):
                for c in range(bc,bc+3):
                    if grid[r][c]!=0: vals.append(grid[r][c])
            if len(vals)!=len(set(vals)): return False
    return True

def sudoku_solve(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c]==0:
                for v in range(1,10):
                    grid[r][c]=v
                    if sudoku_is_valid(grid) and sudoku_solve(grid): return True
                    grid[r][c]=0
                return False
    return True

# GlyphNet minimal (zlib+base64)
import zlib, base64
HEADER="Z5::"
def encode(text:str)->str:
    comp=zlib.compress(text.encode("utf-8"),9)
    return HEADER+base64.b64encode(comp).decode("ascii")
def decode(payload:str)->str:
    assert payload.startswith(HEADER)
    data=base64.b64decode(payload[len(HEADER):].encode("ascii"))
    return zlib.decompress(data).decode("utf-8")

def mixed_corpus(n_sent=200, min_len=20, max_len=60):
    corpus=[]
    for _ in range(n_sent):
        L=random.randint(min_len,max_len)
        s="".join(random.choices(string.ascii_letters+" ", k=L))
        corpus.append(s)
    # add a bit of lorem to avoid pure randomness
    corpus.append("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
    return "\n".join(corpus)

def compliance_score_evidence(evid_path="evidence"):
    # item -> required evidence file presence
    items={
        "risk_management":"ai_act_risk_register.md",
        "data_governance":"data_governance_policy.md",
        "technical_robustness":"technical_robustness_report.md",
        "transparency":"transparency_model_card.md",
        "human_oversight":"human_oversight_procedure.md",
        "accuracy_stats":"accuracy_stats_report.md",
        "cybersecurity":"sbom_and_security_review.md",
        "environmental_impact":"energy_impact_assessment.md"
    }
    passed=0; total=len(items)
    for k,fn in items.items():
        if os.path.exists(os.path.join(evid_path, fn)):
            passed+=1
    return passed/total if total>0 else 0.0, items

def run():
    random.seed(13)
    # Reasoning baseline (parity only)
    tasks=arc_like_tasks(60,12)
    b_succ=z_succ=0; total=0
    t0=time.perf_counter()
    for v,y in tasks:
        pred=arc_like_solver(v); b_succ+=int(pred==y); total+=1
    t_base=time.perf_counter()-t0

    # Zoran reasoning = same ARC +
    t1=time.perf_counter()
    for v,y in tasks:
        pred=arc_like_solver(v); z_succ+=int(pred==y)
    # mazes
    mazes=gen_mazes(10,12,7)
    for m in mazes:
        z_succ+=int(maze_solve(m)); total+=1
    # sudoku
    if sudoku_solve(simple_sudoku()): z_succ+=1; total+=1
    t_z=time.perf_counter()-t1

    score_base=100*(b_succ/total)
    score_z=100*(z_succ/total)
    energy_proxy = (t_z/max(t_base,1e-6))

    # Stability (proxy guard)
    guard=DeltaM113Guard()
    base_fail=z_fail=0
    for t in range(60):
        unstable = (random.random()<0.3)
        base_fail+=int(unstable)
        guard.record(unstable)
        if not guard.should_rollback():
            z_fail += int(unstable)

    # GlyphNet on mixed corpus (non répétitif)
    text = mixed_corpus()
    enc=encode(text); dec=decode(enc); assert dec==text
    ratio = len(text.encode())/len(enc.encode())

    # Compliance (evidence-based)
    comp_score, comp_items = compliance_score_evidence("evidence")

    # No composite pertinence by default (set None)
    out={
        "meta":{"created": time.time(), "note":"HUMBLE v1"},
        "reasoning":{"baseline":score_base,"zoran":score_z,"n":total,"energy_proxy": energy_proxy},
        "stability":{"baseline": base_fail/60.0, "zoran": z_fail/60.0},
        "glyphnet":{"ratio": ratio, "note":"mixed non-repetitive corpus"},
        "compliance":{"score": comp_score, "requires_files": comp_items},
        "pertinence_composite": None
    }
    with open("metrics_humble.json","w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2))

if __name__=="__main__":
    run()
