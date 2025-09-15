# Zoran v31 — Injector TOTAL (Flat)
Date: 2025-09-15T23:30:29.496117Z

## Files
- INJECTOR_TOTAL_SPEC.md — spec complète (Sécurité + Pertinence + Rôle + Traçabilité)
- injector_total_schema.json — schéma JSON
- injector_total.py — implémentation déterministe (HMAC signature)
- injector_total_test.py — tests (sécurité, déterminisme, seuils, schéma-lite)
- RELEVANCE_POLICY.md — seuils & prise de décision
- RELEVANCE_RESULTS_TEMPLATE.json — format standard de scores

## Usage
```bash
export ZORAN_SIGN_KEY='zoran_demo_key'
python injector_total.py                 # crée injector_total_log_31.json
python injector_total_test.py            # exécute tests
```
