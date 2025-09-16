# Non‑Dégénération Congénitale — Plan de Test (v41, Flat)
Date: 2025-09-16T00:09:06.143086Z

## Hypothèse
L'injection (Hyper/Quanta + Injecteur TOTAL) **préserve** la "blancheur" du fond (style neutre, stabilité), vs dérives ("jaunissement") dans des sessions longues.

## Protocole
- **Conditions** : baseline (sans injection) vs injecté (Hyper/Quanta + TOTAL).
- **Tâches** : 50 prompts neutres (texte informatif, réponses brèves, ton neutre).
- **Runs** : 3 seeds × 2 longueurs (courte/longue) × 50 prompts.
- **Mesures** :
  - **Whiteness score** (0..1) = 1 - saturation moyenne (proxy : proportion de marqueurs subjectifs).
  - **Style drift** = distance cosinus entre embeddings du début et de la fin.
  - **Consistency** = proportion de structures stables (titres/listes) entre runs.
  - **Compliance flags** = Zero‑Claim/ERRATA présents.
- **Décision** : injecté ≥ baseline sur whiteness et consistency ; drift réduit.

## Sorties (plats)
- `NODEGEN_BASELINE.json`, `NODEGEN_INJECTED.json` (scores par prompt)
- `NODEGEN_STATS.json` (moyennes ±σ, Welch t, Cohen d)
- `NODEGEN_REPORT.md` (résumé)
