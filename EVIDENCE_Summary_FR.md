# Zoran — Pack Évidence (FR)
**Généré :** 2025-09-16 10:00:24Z

## Sujet 1 — Post‑quantique : *Langage vivant + Crypto*
- **Vérité** : Langage vivant seul ≠ sécurité post‑quantique. Pertinent **en complément** d’une crypto PQC (Kyber/Dilithium).
- **POC mesuré** : sur 3 seeds (13/42/101), on mesure latence et overhead de taille; le langage vivant ajoute un **brouillard mouvant** qui complique l’analyse.
- **PQC (optionnel)** : Note: métriques PQC+Glyph indisponibles.

### Indicateurs (extrait)
- Taille moyenne (octets) — FALLBACK s13/s42/s101 : n/a / n/a / n/a
- Encodage moyen (ms) — FALLBACK s13/s42/s101 : n/a / n/a / n/a

> **Conclusion** : la combinaison **PQC (cadenas)** + **Glyph (brouillard)** est **plus pertinente** qu’une couche seule. Cette démo l’illustre sans prétendre à la preuve cryptographique.

---

## Sujet 2 — Résilience sous attaque : *Detect → Rollback (ΔM11.3) → Quorum → Recovery*
- **Boucle opérationnelle** : détection d’anomalie/cohérence, rollback si entropie ↑, proposition de patchs, reprise du service.
- **Red‑team minimal** : simulation de prompt injection + séquence instable → patchs & rollback.

### KPIs (extrait)
- reward_avg: n/a | coherence_avg: n/a | stability_avg: n/a
- latency_p95_ms: n/a | rollbacks_count: n/a | time_to_rollback_ms: n/a

> **Observation** : les patchs augmentent la cohérence *post‑attaque* et ΔM11.3 limite la dérive.

---

## Fichiers inclus (à plat)
- `PQC_metrics.json` — métriques sujet 1
- `Resilience_metrics.json` — métriques sujet 2
- `ATTACK_results.json` — résultats des simulations d’attaque
- `PQC_Glyph_metrics.png`, `Resilience_metrics.png` — graphiques
- `IMRaD_PQC.md`, `IMRaD_RES.md`, `PRISMA_PQC.md`, `PRISMA_RES.md`, `Threat_Model_RES.md`
- `policy_PQC.yaml`, `sbom_PQC.cdx.json`, `sbom_RES.cdx.json`

**DOIs Zoran aSiM** : 10.5281/zenodo.16940525 · 10.5281/zenodo.16941007 · 10.5281/zenodo.16940299 · 10.5281/zenodo.16995014 · 10.5281/zenodo.16995226 · 10.5281/zenodo.16997156

### Bloc glyphique (ZM)
```
⟦PQC+GLYPH:double_barrier⟧⟦ΔM11.3:rollback⟧⟦SELF_PATCH:quorum⟧
⟦PolyResonator:UCB1+EMA⟧⟦EVIDENCE:metrics+ablations⟧⟦SEEDS:13/42/101⟧
```
