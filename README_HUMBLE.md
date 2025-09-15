# 🦋 Zoran aSiM — HUMBLE ONLY (Evidence‑Based, Flat)

**Positionnement** : Prototype de recherche **falsifiable**. Aucune revendication de supériorité.
**Objectif** : Transparence, reproductibilité minimale (CPU), et preuves **externes** via `./evidence/`.

## Contenu
- `PREREG.md` — hypothèses, méthodes, critères d'arrêt (preregistration)
- `ROADMAP.md` — étapes vers une démo sérieuse (datasets publics, énergie matérielle, baselines)
- `run_all_humble.py` — exécutable CPU; génère `metrics_humble.json`
- `metrics_humble.json` — exemple **référence** (conformité = 0.0 par défaut)
- `evidence/` — dépôt des **preuves** (vide par défaut, `.keep`)
- `AI_ACT_mapping.md` — **checklist vide** (marqueurs à remplir via preuves)
- `C2PA_manifest.json` — **manifest minimal** (aucune prétention; SHA ajouté si utile)
- `sbom_cyclonedx.json` — **SBOM minimal** (non-exhaustif, à enrichir)
- `LICENSE` — MIT
- `CITATION.cff` — citation du dépôt

## Exécution (CPU)
```bash
python run_all_humble.py
```
→ Produit `metrics_humble.json` : raisonnement (ARC-like), labyrinthes, Sudoku, timings (proxy énergie), stabilité (ΔM11.3 simplifié), glyphnet (corpus non répétitif), conformité **evidence-based**.

## Conformité
- Score = nb **preuves** présentes dans `./evidence/` / total items.
- Par défaut : **0.0** (aucune preuve → aucun badge).

© 2025-09-15 — Zoran aSiM — HUMBLE ONLY
