# Zoran v56 — Bench dataset (300 prompts) + runners + merge (Flat)
Date: 2025-09-16T00:46:27.289231Z

## Fichiers plats
- prompts_shard_01.jsonl, _02, _03 (100 prompts chacun)
- run_benchmark_shard.py — runner par shard/seed
- merge_results.py — consolidation globale
- SEEDS_RUNS_PLAN.md — plan seeds/runs
- BENCH_REPORT_v56.md — gabarit rapport

## Exécution (démo)
```bash
python run_benchmark_shard.py --seed 13 --shard prompts_shard_01.jsonl
python merge_results.py
```
