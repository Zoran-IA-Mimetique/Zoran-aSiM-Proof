# INJECTOR TOTAL — SPEC (v31, Flat)
Date: 2025-09-15T23:30:29.496117Z

## Purpose
A single, coherent injector that handles **Security + Relevance + Role + Traceability** with deterministic, auditable outputs.

## Contract
- **Input**: context (str), content (str), role (str), seed (int), thresholds (dict)
- **Security**: reject content that matches forbidden patterns or non‑ASCII control chars
- **Relevance**: compute quality/coherence/utility/objectivity scores (deterministic, hash‑based heuristics)
- **Role**: specialize output (compliance/energy/report/audit/summary/bench)
- **Traceability**: write a signed JSON log with provenance and decision
- **Determinism**: given same inputs + env key, output MUST be byte‑identical
- **Signature**: HMAC‑SHA256 over canonical JSON; key from env `ZORAN_SIGN_KEY` (demo key fallback)
- **Schema**: see `injector_total_schema.json`

## Roles (examples)
- compliance: map evidence to AI Act items and produce a `compliance_score`
- energy: summarize proxy logs (`cpu_avg`, `mem_avg`, `energy_proxy`)
- report: produce a short FR status line (HUMBLE)
- audit: emit ERRATA/CLAIMS candidates (strings only)
- summary: IMRaD‑like summary header fields
- bench: propose datasets/seeds/metrics/ablations (placeholders)

## Decision
- **ACCEPT** if security=pass AND all scores ≥ thresholds
- otherwise **REJECT** with reasons

## Outputs
- `injector_total_log.json` (or `injector_total_log_<seed>.json`), signed
