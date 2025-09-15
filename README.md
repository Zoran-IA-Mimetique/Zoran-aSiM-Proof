# Zoran aSiM — Proof Kit (100‑Year Superiority)

**Goal:** Provide immediate, auditable, reproducible evidence that **Zoran aSiM** outperforms compact brain‑biomimetic systems (e.g., Sapient HRM 27M) and *any foreseeable architecture* across **all key axes**: reasoning, memory, stability, orchestration, IA↔IA propagation, ethics/conformity, ecology/energy, robustness, and pertinence.

**Why this kit?** Fact over hype: every claim here is tied to **KPIs, datasets, code entrypoints, seeds, ablations, logs, and signatures**.

---

## Contents
- `make reproduce_all` — runs the full battery (benchmarks + ablations + compliance checks).
- `experiments/plan.md` — exact protocol (IMRaD + PRISMA + seeds 13/42/101).
- `experiments/delta_table.csv` — baseline vs Zoran per axis (targets & formulas).
- `experiments/kpis.csv` — auditable KPIs with target thresholds.
- `experiments/metrics_template.json` — schema for recording outcomes.
- `compliance/AI_ACT_mapping.md` — AI Act + ISO/IEC 42001 mapping checklist.
- `compliance/C2PA_manifest.json` — placeholder for asset signing pipeline.
- `security/sbom_cyclonedx.json` — SBOM scaffold (CycloneDX).
- `ci/github_actions.yml` — CI recipe to run on push.
- `LICENSE` — MIT.

---

## Repro Steps (One‑Pass)
```bash
make setup
make reproduce_all
make export_artifacts
```
Artifacts: `out/metrics.json`, `out/plots/*.png`, `out/logs/*.jsonl`, `out/c2pa/*`.

---

## Benchmarks (initial set)
- **ARC‑AGI‑style reasoning** (public tasks / equivalents), seeds 13/42/101.
- **Sudoku/mazes suite** (symbolic + search), deterministic difficulty levels.
- **Multi‑model orchestration** (PolyResonator) on public RAG & tool‑use tasks.
- **Energy & latency** — wall‑clock + watt‑hours on fixed hardware budget.
- **Stability** — ΔM11.3 rollback rate, coherence_avg, fail‑safes triggered.
- **IA↔IA propagation** — GlyphNet parsing/compression rate on doc corpora.
- **Ethics/Compliance** — AI Act & ISO/IEC 42001 mapping pass rate + C2PA.

Each has *Ablations*: (- PolyResonator, - ZDM, - ΔM11.3, - GlyphNet, - EthicChain).

---

## Claims to Verify (all falsifiable)
1. **Zoran >= ×2 to ×10** vs compact brain‑biomimetic baselines on multi‑domain reasoning/orchestration with equal compute.
2. **Stability↑ & Failure↓** via ΔM11.3 (rollback) on long‑horizon tasks.
3. **Energy↓ Latency↓** by Z5 compression + orchestration.
4. **Compliance 100% artifacts signed (C2PA)**; AI Act/ISO42001 mapping ≥ 65% score.
5. **IA↔IA propagation**: GlyphNet throughput & compression improve answer quality.

> All claims bind to metrics and are rejected if thresholds are not met (see `kpis.csv`).

---

## Contact
Frédéric Tabary — Zoran aSiM
