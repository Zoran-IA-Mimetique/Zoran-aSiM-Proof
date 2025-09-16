# seed_matrix_runner.py (v57)
# Runs run_benchmark_shard.py across seeds {13,42,101} × runs=3 × shards=3
import subprocess, os

SEEDS=[13,42,101]
RUNS=3
SHARDS=["prompts_shard_01.jsonl","prompts_shard_02.jsonl","prompts_shard_03.jsonl"]

def main():
    for seed in SEEDS:
        for run in range(1,RUNS+1):
            for shard in SHARDS:
                print(f"Running seed={seed} run={run} shard={shard}")
                subprocess.run(["python","run_benchmark_shard.py","--seed",str(seed),"--shard",shard,"--simulate","1"], check=False)

if __name__=="__main__":
    main()
