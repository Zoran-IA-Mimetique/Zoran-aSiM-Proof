# Benchmarks Plan — v40
Date: 2025-09-16T00:06:59.860517Z

## Datasets cibles
- **ARC** : https://github.com/fchollet/ARC (MIT)
- **GSM8K** : https://github.com/openai/grade-school-math (MIT)
- **MMLU** : academic, check licence

## Méthodologie
- **Seeds fixes** : 13, 42, 101
- **Runs** : 3 par seed
- **Métriques** : accuracy, longueur, compliance flags
- **Comparaison** : baseline GPT‑5 vs Zoran injecteur TOTAL
- **Logs** : JSON + SHA manifest

## Étapes
1. Télécharger datasets publics, vérifier licence/checksum.
2. Exécuter baseline GPT‑5.
3. Exécuter GPT‑5 + injecteur TOTAL.
4. Comparer résultats (Welch t, Cohen d).
5. Publier résultats + ERRATA si nécessaire.

⚠️ Zero‑Claim : aucun résultat public tant que non audité par un tiers.
