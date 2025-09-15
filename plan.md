# Experiments Plan (IMRaD + PRISMA + Ablations)

## Introduction
Test Zoran aSiM vs compact brain‑biomimetic baseline on reasoning, memory, stability, orchestration, IA↔IA propagation, ethics/compliance, ecology/energy.

## Methods
- **Design**: Fixed‑budget compute; seeds = 13, 42, 101. 3 runs/seed → mean±σ; Welch t‑tests.
- **Ablations**: -ΔM11.3, -ZDM, -PolyResonator, -GlyphNet, -EthicChain.
- **Datasets**: ARC‑like public tasks; open Sudoku/maze sets; public QA/RAG sets; energy via OS power meter APIs if available or proxy via wall‑clock on fixed HW.
- **Metrics**: see `kpis.csv`; schema `metrics_template.json`.
- **Compliance**: AI Act mapping; C2PA signing flow dry‑run.

## Results (to fill)
Populate `out/metrics.json` via `make reproduce_all`.

## Discussion
Accept/reject claims based on KPIs thresholds; report limitations & compute budget.
