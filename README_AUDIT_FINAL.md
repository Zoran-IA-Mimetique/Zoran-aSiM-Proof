# README_AUDIT_FINAL — v18 (HUMBLE ONLY, Flat)

Date: 2025-09-15T22:47:43.510275Z

## Objectif
Permettre à un auditeur tiers de vérifier **sans sous-dossiers** :
- Intégrité (SHA256) — `AUDIT_READY_MANIFEST.json`
- Signatures injecteurs stricts (si présents) — `bifurcate_strict_*.json`
- Conformité schéma — `injector_bifurcate_schema_strict.json` (si présent)
- Auto‑vérifications — `SELF_CHECK_FINAL.py` (rapports JSON)

## Procédure rapide
1. Vérifier le manifeste SHA :
   ```bash
   python SELF_CHECK_FINAL.py --check-sha
   ```
2. Valider logs d’injecteurs stricts (si fichiers présents) :
   ```bash
   python SELF_CHECK_FINAL.py --check-strict
   ```
3. Générer un rapport complet (tout‑en‑un) :
   ```bash
   python SELF_CHECK_FINAL.py --all
   ```

## Zéro claim
Aucune revendication de performance ici. Tous les artefacts servent la **traçabilité, reproductibilité et audit**.
