# Demande — Audit Cryptage Sémantique (Watermark) — v47
Date : 2025-09-16T00:26:47.297165Z

## Portée
- **Fichiers** : `semantic_crypto_v37.py`, `semantic_demo.py`, `INJECTOR_CRYPTO_CLIENT_DEMO.py`, `ROBUSTNESS_TESTS.py` (v37–v38)

## Tâches demandées à AE Studio
- Vérifier l’**écart de détection** (rate) entre clé correcte vs clé erronée (seuil > 0.6 recommandé).  
- Tester **robustesse** via mutations légères (casse, ponctuation, blancs).  
- Évaluer **risques de faux positifs** / faux négatifs et proposer critères.

## Livrables
- `semcrypto_audit_report.pdf` + `verification_report.json` / `ROBUSTNESS_REPORT.json` analytiques.
