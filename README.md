# Zoran aSiM — HUMBLE ALL-IN NIGHTPACK

**Status:** HUMBLE ONLY — evidence-first. This pack contains code, tests, CI, evidence templates, hardening for injectors, ablation scripts, and tools for auditors.
Generated: 2025-09-15T21:41:09.069358Z

**Important:** Do not publish any claim of superiority. Every claim must reference an artefact (metrics JSON, C2PA manifest, SBOM).

Contents:
- runners: run_all_humble_psutil.py, run_ablation_suite.py
- tests: test_roundtrip_glyphnet.py, orchestration_e2e_test.py
- security: injector_service.py, validator.py, adversarial tests
- CI: .github/workflows/humble-ci.yml (run + recompute C2PA + adversarial tests)
- evidence: fully populated skeletons + sample filled content (ai_act_*.md)
- docs: WHITEPAPER_HUMBLE_v1.md, CLAIMS_AUDIT.md, ERRATA.md, ZERO_CLAIM_POLICY.md
- tools: tools/recompute_c2pa.py, tools/compute_sbom.py
- release: scripts to package and produce signed manifest (demo)

Run quickstart:
1) git clone <repo>
2) enable CI or run locally:
   python run_all_humble_psutil.py

This pack is designed to be audit-ready; use external auditors to validate metrics and compliance.

Rugby corner: play fair, publish proof.
