
# 🦋 Zoran aSiM — Research Prototype Kit (HUMBLE v1, flat)

**Positionnement honnête** : ceci est un **prototype de recherche**, pas une preuve de supériorité.
- Pas de claims marketing (“100 ans”, “supériorité”) — **retirés**.
- Objectif : **transparence, reproductibilité, falsifiabilité**.

## Ce que contient ce kit
- **Code exécutable (CPU)** minimal pour tester des idées (ΔM11.3, ZDM, GlyphNet, PolyResonator).
- **Mesures réelles** de temps (proxy énergie) + **metrics.json**.
- **Conformité** en mode *evidence-based* : chaque item AI Act/ISO nécessite un **fichier de preuve** dans `./evidence/`.
- **Preregistrations** & protocole (PREREG.md) pour éviter le p-hacking.
- **ROADMAP.md** : étapes pour passer d’un POC honnête à une démo sérieuse.

## Exécution (CPU)
```bash
python run_all_humble.py
```
→ Produit `metrics_humble.json` avec : raisonnement, stabilité, glyphnet (corpus mixte **non répétitif**), conformité (score basé sur preuves présentes), pertinence_composite **désactivée par défaut**.

## Conformité (evidence-based)
- **AI Act / ISO 42001** : un item ne peut être “PASS” que s’il existe un fichier de preuve dans `./evidence/` (ex. `evidence/ai_act_risk_register.md`).
- Par défaut, **score = 0.0** (aucune preuve). **On ne badge pas.**

## Note sur GlyphNet
- Compression évaluée sur un **corpus mixte** peu répétitif (phrases aléatoires + lorem). Les ratios attendus sont modestes (~1.0–1.5). Pas de “×50” ici.
- GlyphNet n’est **pas** présenté comme percée — juste un **codec IA↔IA expérimental**.

## Limites reconnues
- Benchmarks simples → **à étendre** avec datasets publics référencés.
- Énergie = proxy temps → **à remplacer** par mesures matérielles.
- Pas de baseline Sapient HRM → **à implémenter** (ou protocole de réplication).

---

© 2025-09-15 — Zoran aSiM (Prototype de recherche, HUMBLE v1)
