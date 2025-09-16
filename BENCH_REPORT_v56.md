# Benchmarks v56 — Rapport Global (Flat)
Date: 2025-09-16T00:46:27.289231Z

## Seeds & Runs
- Seeds : 13, 42, 101 ; Runs : 3 par seed (recommandé)  
- Shards : 3 × 100 prompts = 300 prompts

## Procédure
```bash
python run_benchmark_shard.py --seed 13 --shard prompts_shard_01.jsonl
python run_benchmark_shard.py --seed 13 --shard prompts_shard_02.jsonl
python run_benchmark_shard.py --seed 13 --shard prompts_shard_03.jsonl
# répéter pour seeds 42, 101
python merge_results.py
# -> BENCH_STATS_GLOBAL.json
```

## À compléter
- Coller BENCH_STATS_GLOBAL.json ci-dessous
- Analyser les deltas (ok, pertinence) et limites
