# Demande d’évaluation indépendante — AE Studio (Master) — v47 (Flat)
Date : 2025-09-16T00:26:47.297165Z

## Contexte
- **Projet** : Zoran aSiM — surcouche mimétique, éthique et traçable au‑dessus d’un LLM SOTA (ex. GPT‑5).  
- **Dépôt GitHub** : [insérer lien public]  
- **Politique** : Zero‑Claim (aucune assertion de performance sans protocole public + artefacts reproductibles + audit tiers).

## Objectifs d’évaluation
1) **Injecteur TOTAL** — Sécurité + Pertinence + Rôle + Traçabilité  
   - Vérifier les contrôles de sécurité (patterns interdits, ASCII).  
   - Éprouver les **métriques de pertinence** (quality/coherence/utility/objectivity) et la **décision par seuils**.  
   - Confirmer le **déterminisme** et la **signature HMAC** (anti‑tamper).

2) **GlyphNet** — Codec IA↔IA (Z5:: zlib+base64)  
   - Lancer un **benchmark reproductible** vs gzip/xz sur un corpus plat et public.  
   - Rapporter **taille**, **temps enc/dec**, limites.

3) **Cryptage sémantique (watermark lexical)**  
   - Vérifier la **détection** clé correcte vs clé erronée (écart significatif).  
   - Tester la **robustesse** (mutations légères).  
   - Rappeler : provenance ≠ confidentialité (crypto forte côté client pour secret).

4) **Non‑dégénération & Propagation IA↔IA**  
   - Exécuter les **simulateurs** (whiteness/drift/consistency, parse‑rate/retention) comme POC méthodo.  
   - Proposer un protocole “réel” pour la suite (si pertinent).

## Livrables attendus
- Rapport signé (PDF) avec **constats, preuves, limites, recommandations**.  
- Artefacts : JSON/CSV de résultats + scripts/commandes exactes.  
- Statut : **Pass / Partial / Fail** par objectif.

## Cadre
- Pas d’accès à données privées.  
- Scripts plats, seeds fixes, SHA manifest, CI possible.  
- Contrats : NDA si requis (cf. AISTUDIO_NDA_NOTE.md).
