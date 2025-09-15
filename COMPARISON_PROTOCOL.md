# SOTA COMPARISON PROTOCOL (Draft)

1) **Tâches & Données**
   - Datasets publics référencés + licences (ex: ARC-officiel, GSM8K, Maze datasets, Sudoku standard).
   - Splits fixes; pas de fuite de test.

2) **Compute & Budget**
   - Matériel documenté, budget temps/énergie fixé.
   - Journalisation énergie: wattmètre si possible; sinon psutil + intervalle.

3) **Seeds & Stats**
   - Seeds ≥ {13,42,101}, 3 runs/seed → moyenne ±σ; Welch t-test p<0.05.

4) **Ablations**
   - −ΔM11.3, −ZDM, −Orchestration, −GlyphNet (et combinaisons).

5) **Artefacts**
   - `metrics.json`, logs, scripts, C2PA manifest, SBOM, PREREG, README, ROADMAP.

6) **Review**
   - Revue ouverte (issues/PR); reproduction indépendante encouragée.
