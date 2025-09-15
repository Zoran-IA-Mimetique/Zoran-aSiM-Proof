# KPIs & Metrics — Definitions

- **score_idx (Reasoning MD)**: mean task success (%) over a fixed public suite (ARC-like 200 tasks, Sudoku 100, Mazes 100). Each task is success=1/0. Index = 100 × successes / total. Baseline normalized to 100.
- **rollback_fail_rate**: fraction of long-horizon steps that require ΔM11.3 rollback. Lower is better.
- **task_success (Orchestration)**: success index (%) on tool-use/RAG mixed tasks with PolyResonator enabled.
- **glyphnet_throughput**: effective compression × parsing throughput (tokens/hour) on `.zgs` corpora; reported as ratio vs baseline (1.0).
- **compliance_score**: normalized score [0,1] computed as (# items “pass” in AI Act + ISO/IEC 42001 checklist) / (total items).
- **watt_hours**: energy consumed to reach target accuracy on fixed hardware; normalized vs baseline (=1.0).
