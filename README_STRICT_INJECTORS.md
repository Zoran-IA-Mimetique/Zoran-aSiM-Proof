# README_STRICT_INJECTORS — v16

Date: 2025-09-15T22:39:38.574132Z

## What "perfect" means here
- Deterministic, schema-valid, signed, tamper-detectable, CI-tested.
- No performance claims: outputs are traceable logs, not marketing.

## Quickstart
```bash
export ZORAN_SIGN_KEY='zoran_demo_key'
python injector_bifurcate_strict.py compliance,energy,report strict_demo_ctx 16
python validate_bifurcate_strict.py bifurcate_strict_16.json
python tests_injectors_strict.py
```
Artifacts: `bifurcate_strict_16.json`, `STRICT_TEST_REPORT.json`, `VALIDATE_STRICT_RESULT.json`

