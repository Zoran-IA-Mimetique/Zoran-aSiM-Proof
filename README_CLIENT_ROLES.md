# README_CLIENT_ROLES — v13 (HUMBLE ONLY)

Date: 2025-09-15T22:28:42.283187Z

## Rôles & injecteurs (cartographie)
- **STEM (cellule souche)** → injecteur générique (glyphnet) capable de se spécialiser.
- **Compliance** → mapping evidence ↔ AI Act/ISO, score documentaire.
- **Energy** → analyse de logs psutil (cpu/mem), proxy énergie.
- **Report** → synthèse client FR (HUMBLE), preuves présentes/absentes.
- **Audit** → ERRATA/CLAIMS_AUDIT, cohérence preuves ↔ annonces.
- **Summary** → IMRaD + limites.
- **Bench** → protocole reproductible (datasets, seeds, stats, ablations).

## Fichiers utiles (tous à la racine)
- `stem_specializations.py` → génère des logs JSON structurés par rôle
- `injector_log_schema.json`, `TEMPLATE_INJECTOR_LOG.json` → schéma & modèle
- `validate_injector_log.py` → vérifie la conformité d’un log au schéma
- `C2PA_manifest_full.json` → manifeste des artefacts (hashes), regénéré v13
