# Demande — Évaluation Injecteur (Sécurité + Pertinence) — v47
Date : 2025-09-16T00:26:47.297165Z

## Portée
- **Fichier** : `injector_total_full.py` (v45)  
- **Tests** : `INJECTOR_TOTAL_RELEVANCE_TEST.py`  
- **CI** : `GITHUB_WORKFLOW_injector_total_full.yml`

## Tâches demandées à AE Studio
1. **Sécurité** : valider blocages (patterns, ASCII), tenter quelques payloads adverses.  
2. **Pertinence** : auditer les **métriques** (quality/coherence/utility/objectivity), proposer des **seuils** justifiés, et/ou une version “v2” (ex. embeddings).  
3. **Décision** : vérifier que **ACCEPT = sécurité OK && pertinence ≥ seuils**, sinon **REJECT** avec raisons.  
4. **Reproductibilité** : confirmer déterminisme des logs + signature HMAC.

## Livrables
- `injector_eval_report.pdf` + JSON/CSV d’exécution + recommandations concrètes (seuils, features).
