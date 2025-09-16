# Plan Benchmarks Internes — France Travail (v51, Flat)
Date : 2025-09-16T00:34:54.427975Z

## Objectif
Permettre à France Travail d’évaluer Zoran aSiM sur leurs datasets internes, **sans fuite de données**.

## Protocole
- **Exécution locale** : scripts plats fournis, pas de transfert externe.  
- **Seeds fixes** : 13, 42, 101 (3 runs).  
- **Métriques** : accuracy, longueur, pertinence scores (injecteur TOTAL).  
- **Artefacts attendus** : JSON de résultats + SHA manifest.  
- **Conformité** : aucune donnée personnelle transmise, NDA respecté.

## Étapes
1. Préparer dataset interne (textes métiers anonymisés).  
2. Lancer injecteur TOTAL (`injector_total_full.py`).  
3. Générer `BENCH_CLIENT_RESULTS.json`.  
4. Vérifier intégrité avec SHA.  
5. Compiler rapport interne.  
