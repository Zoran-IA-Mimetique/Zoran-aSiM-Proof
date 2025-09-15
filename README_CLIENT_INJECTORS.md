# README_CLIENT_INJECTORS — v12 (HUMBLE ONLY)

Date: 2025-09-15T22:26:35.026278Z

## Objet
Expliquer aux équipes France Travail comment fonctionnent les **injecteurs “cellules souches”** (STEM) et leurs spécialisations (compliance, energy, report).

## Comment ça marche (simple)
- Un injecteur **STEM** (bloc glyphique) sert de base.
- On le **spécialise** en un rôle : `compliance`, `energy`, `report`.
- Le script `stem_specializations.py` génère un **log JSON** conforme au schéma `injector_log_schema.json`.

## Exemples d’exécution
```bash
python stem_specializations.py compliance   # -> injector_compliance_log.json
python stem_specializations.py energy       # -> injector_energy_log.json
python stem_specializations.py report       # -> injector_report_log.json
```

## Ce que **ce n’est pas**
- Pas une preuve de supériorité : ce sont des **logs structurés** d’un mécanisme de différenciation, pas un benchmark.

## Pourquoi c’est utile
- **Traçabilité** : chaque spécialisation produit un JSON auditable (C2PA possible).
- **Méthode** : aligne l’IA sur un rôle **sans changer de modèle**, utile pour conformité, énergie, reporting client.
