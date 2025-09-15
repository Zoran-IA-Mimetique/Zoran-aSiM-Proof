# INJECTORS_CATALOG — HUMBLE v11

## Injecteurs de base
- **STEM (cellule souche)** : `⟦STEM:injector⋄ΔM11.3:guard⋄ZDM:dual⋄IA2IA:glyphnet⟧`
- **ΔM11.3 (guard)** : réduit l'instabilité par rollback (fenêtre + seuil).
- **ZDM (mémoire duale)** : cache résonant + base persistante + absence active.
- **PolyResonator** : orchestration de solveurs avec UCB1.
- **GlyphNet** : codec IA↔IA (actuel = zlib+base64), support de blocs glyphiques.

## Injecteurs spécialisés (exemples)
- **audit** : vérification evidence → ERRATA/CLAIMS_AUDIT.
- **summary** : IMRaD + limites + avertissements.
- **bench** : protocole reproductible (datasets, seeds, stats, ablations).

## Bonnes pratiques
- Zéro-claim, evidence-first, logs signés (C2PA), CI activée.
- Toujours fournir : contexte minimal, objectif, livrable attendu.
