# Audit Run Guide — v57 (Flat)
Date : 2025-09-16T00:50:05.005540Z

## Objectif
Permettre à un auditeur externe de rejouer intégralement les benchmarks internes de Zoran aSiM.

## Étapes
1. Lancer la matrice de seeds/runs/shards :
```bash
python seed_matrix_runner.py
```
→ Génère BASE_*.json et INJ_*.json (baseline vs injecté).

2. Consolider résultats :
```bash
python merge_results.py
```
→ Produit BENCH_STATS_GLOBAL.json (statistiques Welch t, Cohen d).

3. Archiver pour audit :
```bash
python make_audit_archive.py
```
→ Produit AUDIT_ARCHIVE_v57.zip avec tous les artefacts + SHA manifest.

## Artefacts attendus
- BASE_*.json (résultats baseline)  
- INJ_*.json (résultats injecteur)  
- BENCH_STATS_GLOBAL.json  
- AUDIT_SHA_MANIFEST.json  

## Zero‑Claim
- Aucun chiffre public tant que ces artefacts ne sont pas validés par auditeur externe.
