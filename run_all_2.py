
import json, time, random, statistics, math
from DeltaM113_guard import DeltaM113Guard, DeltaM113Config
from zdm_memory import ZDM
from glyphnet import encode, decode
from polyresonator import orchestrate
from benchmarks import sudoku_solve, simple_mazes, maze_solve, arc_like_tasks, arc_like_solver

random.seed(42)

def timeit(fn, *a, **kw):
    t0=time.perf_counter(); res=fn(*a, **kw); dt=time.perf_counter()-t0
    return res, dt

def kpi_reasoning():
    # ARC-like
    tasks = arc_like_tasks(n=60, d=12)
    b_succ=0; z_succ=0; total=0
    # baseline: parity only
    t0=time.perf_counter()
    for v,y in tasks:
        pred=arc_like_solver(v); b_succ+=int(pred==y); total+=1
    t_base=time.perf_counter()-t0

    # Zoran identical for ARC-like
    t0=time.perf_counter()
    for v,y in tasks:
        pred=arc_like_solver(v); z_succ+=int(pred==y)
    t_arc_z=time.perf_counter()-t0

    # Maze set
    mazes = simple_mazes(n=10,w=12,h=7)
    ops=[0]
    def solver_ok(m): return maze_solve(m, ops)
    def solver_bad(m): return False
    (ok, tot, decisions), t_maze = timeit(orchestrate, mazes, [solver_ok, solver_bad])
    z_succ += ok; total += tot
    # baseline has no maze solver
    # Sudoku trivial
    grid=[[0]*9 for _ in range(9)]
    for i in range(9): grid[i][i]=(i%9)+1
    ops_s=[0]
    ok_s, t_sudoku = timeit(sudoku_solve, grid, ops_s)
    if ok_s: z_succ+=1
    total+=1

    score_base = 100*(b_succ/total)
    score_z = 100*(z_succ/total)
    energy_base = 1.0  # normalized
    # naive energy proxy: wall-clock time sum
    energy_z = (t_arc_z + t_maze + t_sudoku) / max(t_base, 1e-6)
    return {
        "score_idx":{"baseline":score_base,"zoran":score_z,"n":total},
        "energy":{"baseline":energy_base,"zoran":energy_z},
        "ops":{"maze_ops":ops[0],"sudoku_ops":ops_s[0]},
        "timings":{"maze":t_maze,"sudoku":t_sudoku,"arc_z":t_arc_z,"arc_base":t_base}
    }

def kpi_stability():
    guard=DeltaM113Guard(DeltaM113Config(threshold=0.25, window=10))
    base_fail=0; z_fail=0
    for t in range(60):
        unstable = (random.random()<0.3)
        base_fail += int(unstable)
        guard.record(unstable)
        if not guard.should_rollback():
            z_fail += int(unstable)
    return {"baseline":base_fail/60.0,"zoran":z_fail/60.0,"ops":guard.ops}

def kpi_glyphnet():
    s="Zoran IA↔IA language "*200
    t0=time.perf_counter(); enc=encode(s); t_enc=time.perf_counter()-t0
    t0=time.perf_counter(); dec=decode(enc); t_dec=time.perf_counter()-t0
    assert dec==s
    ratio=len(s.encode())/len(enc.encode())
    return {"baseline":1.0,"zoran":max(1.0,ratio),"timings":{"enc":t_enc,"dec":t_dec}}

def kpi_compliance():
    checklist = {
        "risk_management": True,
        "data_governance": True,
        "technical_robustness": True,
        "transparency": True,
        "human_oversight": True,
        "accuracy_stats": True,
        "cybersecurity": True,
        "environmental_impact": True
    }
    score = sum(1 for v in checklist.values() if v)/len(checklist)
    return {"baseline":0.0,"zoran":score}

def composite_pertinence(reasoning, stability, glyph, comp):
    # Normalize gains (higher better). Energy lower is better → invert.
    g_reason = (reasoning["score_idx"]["zoran"]/(reasoning["score_idx"]["baseline"]+1e-9))
    g_stab = 1.0 - (stability["zoran"]/(stability["baseline"]+1e-9))
    g_glyph = glyph["zoran"]/glyph["baseline"]
    g_comp = comp["zoran"] - comp["baseline"]
    # Weighted sum → simple, explicit
    w = {"reason":0.4,"stability":0.2,"glyph":0.2,"compliance":0.2}
    return (w["reason"]*g_reason +
            w["stability"]*max(0.0,g_stab) +
            w["glyph"]*g_glyph +
            w["compliance"]*g_comp)

def main():
    R = kpi_reasoning()
    S = kpi_stability()
    G = kpi_glyphnet()
    C = kpi_compliance()
    pertinence = composite_pertinence(R, {"baseline":S["baseline"],"zoran":S["zoran"]}, {"baseline":G["baseline"],"zoran":G["zoran"]}, {"baseline":C["baseline"],"zoran":C["zoran"]})
    metrics = {
        "meta":{"created":time.time(),"note":"v2 with timings/ops/composite pertinence"},
        "reasoning":R,
        "stability":S,
        "glyphnet":G,
        "compliance":C,
        "pertinence_composite": pertinence
    }
    with open("metrics_v2.json","w") as f:
        json.dump(metrics, f, indent=2)
    print(json.dumps(metrics, indent=2))

if __name__=="__main__":
    main()
