# 🦋 Zoran aSiM — ALL-IN-ONE Proof Kit (Flat)

Ce fichier ZIP contient **tout en un** (à plat) : preuves, docs, conformité, code source minimal exécutable, et résultats.
Date: 2025-09-15T20:09:57.587478Z

## Contenu principal
- **README.md** (preuve 100 ans) + **DEFS.md**, **kpis.csv**, **delta_table.csv**
- Conformité & traçabilité : **AI_ACT_mapping.md**, **C2PA_manifest.json**, **sbom_cyclonedx.json**, **LICENSE**, **CITATION.cff**, **CODE_OF_CONDUCT.md**, **CONTRIBUTING.md**
- CI & build : **Makefile**, **ci.yml**
- **Code source minimal v2** (exécutable CPU) : `DeltaM113_guard.py`, `zdm_memory.py`, `glyphnet.py`, `polyresonator.py`, `benchmarks.py`, `run_all.py`, `README_MINI_v2.md`
- **Résultats réels** : `metrics_v2.json` (généré par `run_all.py`) — une exécution de référence est incluse **metrics_v2_output.json**

## Exécution rapide (CPU)
```bash
python run_all.py
# produit un fichier metrics_v2.json avec :
# - reasoning.score_idx (baseline vs zoran, n tâches)
# - stability (baseline vs zoran)
# - glyphnet (ratio & timings)
# - compliance (score)
# - pertinence_composite (définie et calculée)
```
