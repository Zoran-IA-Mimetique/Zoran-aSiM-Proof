# 🦋 Zoran aSiM — ALL‑IN‑ONE FUSION (Flat)

**Date**: 2025-09-15T20:16:32.280244Z

Ce kit fusionne **la branche “preuve ambitieuse”** et **la branche “humble evidence‑based”** en un seul paquet **à plat**.

## 📦 Contenu (principaux fichiers)
- **Ambitious / Proof**: `README.md`, `DEFS.md`, `kpis.csv`, `delta_table.csv`, `AI_ACT_mapping.md`, `C2PA_manifest*.json`, `sbom_cyclonedx*.json`, `CITATION.cff`, `LICENSE`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `Makefile`, `ci.yml`.
- **Humble / Evidence‑Based**: `README_HUMBLE.md`, `PREREG.md`, `ROADMAP.md`, `run_all_humble.py`, dossier `evidence/` (**vide** à compléter).
- **Source runnable (CPU)**: `run_all.py`, `benchmarks.py`, `DeltaM113_guard.py`, `zdm_memory.py`, `glyphnet.py`, `polyresonator.py`, `README_MINI_v2.md`.
- **Résultats**: `metrics_v2_output.json` (exécution de référence v2).

## 🧭 Règles de lecture
- **Aucune supériorité n’est revendiquée sans preuve exécutée.**
- La partie “ambitieuse” donne la **structure** (KPIs, tables, conformité), la partie “humble” impose la **falsifiabilité** (evidence‑based, prereg, pas de composite par défaut).

## ▶️ Exécution (CPU)
- Runner ambitieux (v2, timings & pertinence composite documentée) :
  ```bash
  python run_all.py
  ```
  → produit `metrics_v2.json` (à exécuter localement).

- Runner humble (evidence‑based, corpus non répétitif, pertinence désactivée) :
  ```bash
  python run_all_humble.py
  ```
  → produit `metrics_humble.json`.

## ✅ Conformité (evidence‑based)
- Un item **AI Act / ISO 42001** ne peut être “PASS” que si **une preuve** correspondante est déposée dans `./evidence/`.
- Par défaut, **score = 0.0** (aucune preuve fournie).

## 🔄 Gestion des doublons
Certains fichiers peuvent exister en plusieurs variantes (suffixe `_2`, etc.). Dans ce cas, gardez la version la plus récente/pertinente pour votre usage et supprimez le reste.

---
© Zoran aSiM — ALL‑IN‑ONE FUSION
