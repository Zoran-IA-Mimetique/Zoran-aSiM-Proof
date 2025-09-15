# Zoran aSiM — HUMBLE ONLY v5 (Client-Facing Overview)

Date: 2025-09-15T21:45:43.870147Z

## What this pack is
- A HUMBLE, **evidence-based** prototype: no SOTA claims, only reproducible artefacts.
- Includes code (CPU runners), artefacts (metrics, ablations, logs), manifests (C2PA, SBOM), and governance docs (ERRATA, CLAIMS_AUDIT, ZERO_CLAIM_POLICY).

## What is proven
- Runner scripts execute and produce metrics (`metrics_humble_psutil.json`, `ablation_results.json`, etc.).
- GlyphNet roundtrip test works (`roundtrip_results.json`).
- Orchestration simulation logs present (`orchestration_log.json`).
- Adversarial fuzz tests executed (`adversarial_tests_summary.json`).
- C2PA manifest computed over all repo files.

## What is not proven
- Any performance superiority vs SOTA models (retracted).
- Energy efficiency validated with wattmeter (proxy only).
- Compliance confirmed externally (documents exist but require external audit).

## Immediate actions suggested to client (France Travail)
1. Treat this pack as **audit-ready prototype**, not as final validated solution.
2. Commission independent auditors (RFP provided in `RFP_AUDIT_INDEPENDANT.md`).  
3. Review ERRATA and CLAIMS_AUDIT for withdrawn claims and pending work.  
4. Run included CI workflow on GitHub to regenerate artefacts and manifests automatically.  

## Key artefacts included
- `metrics_humble_psutil.json`
- `ablation_results.json`
- `roundtrip_results.json`
- `orchestration_log.json`
- `adversarial_tests_summary.json`
- `C2PA_manifest_full.json`
- `sbom_cyclonedx_full.json`
- `evidence/*.md` (8 filled docs)

---
© 2025 — MIT License (see LICENSE)

## v7 Update — Injector & Dataset
- `test_injector.py` added: roundtrip & validation checks.
- `dataset_loader.py` added: ARC-like skeleton (replace with public dataset).

## v9 Update — Public-like Datasets
- sudoku_loader.py: generates toy sudoku puzzles.
- maze_loader.py: generates stable mazes with seed.
- run_dataset_bench.py: integrates both datasets, produces dataset_bench_results.json.
