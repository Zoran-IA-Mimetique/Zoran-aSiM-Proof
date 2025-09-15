# Preregistration — HUMBLE ONLY

## Hypothèses (falsifiables)
H1: ΔM11.3 (guard) réduit le taux d'échec sur séquences longues vs. sans guard.
H2: Un orchestrateur simple améliore le taux de réussite sur tâches hétérogènes vs. single-solver.
H3: GlyphNet (~codec) apporte un gain de compression **modeste** sur corpus non répétitif.

## Méthodes
- Seeds fixes 13/42/101; 3 runs/seed → moyenne ±σ.
- Benchmarks publics simples (ARC-like, mazes, sudoku). Licences à documenter.
- Énergie = **proxy temps** (perf_counter) en attendant wattmètre/psutil.
- Conformité = **evidence-based** : PASS seulement si un fichier est déposé dans `./evidence/`.

## Critères d'arrêt
- Publication des résultats **même si négatifs**.
- Pas d'ajustement des pondérations post-hoc.
