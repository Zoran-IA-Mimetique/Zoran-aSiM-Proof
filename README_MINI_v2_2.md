# Zoran aSiM — MINI Source Proof v2 (Runnable)

Améliorations vs v1 :
- Benchmarks élargis (mazes×10, ARC-like×60), Sudoku avec comptage d'opérations.
- Mesures **réelles** de temps (perf_counter) → proxy énergie.
- **Pertinence composite** définie comme combinaison pondérée (raisonnement, stabilité, IA↔IA, conformité).
- Sortie `metrics_v2.json` documentée.

Exécution :
```bash
python run_all.py
```
Fichiers produits : `metrics_v2.json` (et `metrics.json` en v1 si besoin).
