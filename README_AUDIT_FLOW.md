# README_AUDIT_FLOW — v14 (HUMBLE ONLY)

Date: 2025-09-15T22:31:23.375211Z

## Objectif
Fournir à un auditeur tiers un **parcours clair** pour vérifier le pack HUMBLE :
1. **Traçabilité** (C2PA/SBOM/SHA)
2. **Présence des preuves** (evidence)
3. **Exécutabilité** (scripts & artefacts)
4. **Cohérence documentaire** (ERRATA/CLAIMS_AUDIT)

## Étapes
1. **Hashes & manifeste**
   - Ouvrir `ROOT_SHA256_MANIFEST_v13.json` ou `v12/v11` selon la version.
   - Ouvrir `C2PA_manifest_full.json` (v13 regénéré).
   - Vérifier l’intégrité (hashes cohérents après extraction).

2. **Evidence documentaire**
   - Lire `evidence_model_card_full.md`, `evidence_data_processing_register.md`, `NO_BENCHMARK_NOTICE.md`.
   - Noter les preuves **absentes** (ex. benchmark public, audit externe).

3. **Exécution scripts (optionnel)**
   - `python system_info.py` → `system_info.json`
   - `python energy_logger.py 10 0.5` → `energy_log.json`
   - `python stem_specializations.py compliance` → `injector_compliance_log.json`
   - `python validate_injector_log.py injector_compliance_log.json` → `VALIDATION_RESULT.json`

4. **Ablations & métriques**
   - (Si pack technique complet) : `python run_ablation_suite.py` → `ablation_results.json/csv`, `ABLATION_STATS.csv/md`

5. **Rapport d’audit**
   - Structurer les constats : présent / manquant / incohérent / recommandations.
   - (Optionnel) signer le PDF final (hors scope HUMBLE).

## Règles de fond
- **Zero-Claim** : aucune supériorité annoncée ici.
- **Evidence-first** : toute affirmation pointe vers un fichier concret.
