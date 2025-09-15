# 🦋 Zoran aSiM — HUMBLE ONLY (Evidence-Based Research Prototype)

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
<!-- Badges activables quand les preuves sont déposées :
![AI Act](https://img.shields.io/badge/AI%20Act-evidence--based-lightgrey)
![ISO 42001](https://img.shields.io/badge/ISO-42001-evidence--based-lightgrey)
![C2PA](https://img.shields.io/badge/C2PA-manifest_ready-lightgrey)
-->

## 📌 TL;DR (≤150c)
Prototype **ouvert, falsifiable, reproductible**. Zéro claim. Preuves **evidence-based** uniquement. Objectif : méthode solide > promesses.

---

## 🎯 Pourquoi “HUMBLE ONLY” ?
- **Pas** une IA SOTA : c’est un **prototype de recherche** qui démontre des concepts (ΔM11.3, ZDM, PolyResonator, GlyphNet) en version **minimale**.  
- **Zéro-claim policy** : aucune supériorité annoncée sans protocole public + résultats reproductibles.  
- **Conformité** : score = **0.0** par défaut, n’augmente **que** si des preuves concrètes sont déposées dans `./evidence/`.

---

## 📦 Contenu (flat, prêt à publier)
- **Code CPU runnable** : `run_all_humble.py` (raisonnement simple, 10 mazes, 1 sudoku, timings proxy énergie, ΔM11.3 simplifié, GlyphNet non répétitif).  
- **Sorties de référence** : `metrics_humble.json` (exemple).  
- **Méthodologie** : `PREREG.md` (hypothèses, méthodes, critères d’arrêt), `ROADMAP.md` (étapes vers preuve sérieuse).  
- **Conformité evidence-based** : `AI_ACT_mapping.md` (checklist vide par défaut), dossier `evidence/` (**vide** à remplir).  
- **Traçabilité** : `C2PA_manifest.json` (minimal), `sbom_cyclonedx.json` (minimal), `LICENSE` (MIT), `CITATION.cff`.

---

## ▶️ Exécution locale (CPU)
```bash
python run_all_humble.py
```

---

## 🧪 Ce qui est **validé** (prototype) / **non validé**
- ✅ ΔM11.3 (rollback guard) — existe, démonstration jouet  
- ✅ ZDM (mémoire duale) — existe, basique  
- ✅ PolyResonator (UCB1) — existe, orchestration solvers jouets  
- ✅ GlyphNet (codec) — existe, pas d’avantage prouvé  
- ⚠️ Énergie réelle — proxy seulement  
- ⚠️ Conformité AI Act / ISO — score=0.0, à prouver  
- ❌ Supériorité SOTA — retirée (ERRATA)

---

## 🗂️ Evidence-based compliance (AI Act / ISO 42001)
**Règle :** un item n’est “PASS” **que si** le fichier correspondant est présent dans `./evidence/`.

- Risk management → `evidence/ai_act_risk_register.md`  
- Data governance → `evidence/data_governance_policy.md`  
- Technical robustness → `evidence/technical_robustness_report.md`  
- Transparency → `evidence/transparency_model_card.md`  
- Human oversight → `evidence/human_oversight_procedure.md`  
- Accuracy & stats → `evidence/accuracy_stats_report.md`  
- Cybersecurity & SBOM → `evidence/sbom_and_security_review.md`  
- Environmental impact → `evidence/energy_impact_assessment.md`

---

## 🏉 Rugby corner (scrum ≠ bullshit)
On pose le ballon (preuves), on transforme (repro), on score (audit).  
Pas d’essais fantômes : si l’arbitre siffle, on recule et on repart propre.

---

## 📜 Licence
MIT — utilisation libre, responsabilité partagée.
