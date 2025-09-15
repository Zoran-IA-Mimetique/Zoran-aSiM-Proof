
# Preregistration (HUMBLE v1)

## Hypothèses
H1: Un orchestrateur simple (UCB1) améliore le taux de succès sur un ensemble de tâches hétérogènes vs. single-solver baseline.
H2: Un guard ΔM11.3 réduit le taux d'échec sur séquences longues vs. sans guard.
H3: Un codec symbolique (GlyphNet) améliore légèrement l'efficacité IAxIA (compression) sur corpus mixte non répétitif.

## Méthodes
- Seeds fixes (13/42/101) — 3 runs/seed → moyenne ±σ.
- Benchmarks: labyrinthes générés, Sudoku trivial, tâches parité “ARC-like” (corpus simple).
- Énergie: proxy temps (perf_counter) en attendant wattmètre.
- Conformité: items AI Act/ISO marqués PASS **uniquement s'il existe une preuve** dans `./evidence/`.

## Critères d'arrêt
- Publier **même si résultats négatifs**.
- Pas d’ajustement de pondérations post-hoc.
