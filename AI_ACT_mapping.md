# AI Act + ISO/IEC 42001 — Mapping (Detailed Checklist)

## AI Act Core (High-Level)
- Risk management (Art. 9): PASS/FAIL — Evidence: risk register, rollback ΔM11.3 logs.
- Data governance (Art. 10): PASS/FAIL — Evidence: datasets list, licenses, PII minimization.
- Technical robustness (Art. 15): PASS/FAIL — Evidence: ablations, seeds, stability metrics.
- Transparency (Art. 13): PASS/FAIL — Evidence: README, metrics.json, model cards.
- Human oversight (Art. 14): PASS/FAIL — Evidence: reviewer steps, override procedures.
- Accuracy (Annex): PASS/FAIL — Evidence: aggregated means±σ, Welch tests.
- Cybersecurity (Art. 15): PASS/FAIL — Evidence: SBOM CycloneDX, supply-chain checks.
- Environmental impact (Recital): PASS/FAIL — Evidence: watt_hours vs baseline.

## ISO/IEC 42001 (Selected Controls)
- Context & scope defined — PASS/FAIL
- Leadership & policy (ethics) — PASS/FAIL (EthicChain/Aegis Layer stated)
- Planning (risk/opportunities) — PASS/FAIL
- Support (competence, documentation) — PASS/FAIL
- Operation (controls & procedures) — PASS/FAIL
- Performance evaluation (KPIs) — PASS/FAIL
- Improvement (corrective actions) — PASS/FAIL

> Compute **compliance_score** as (#PASS) / (#TOTAL).
