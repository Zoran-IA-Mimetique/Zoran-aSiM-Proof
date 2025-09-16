# Risques et limitations — v54
Date: 2025-09-16T00:40:41.709695Z

1. Limitation fondamentale: l'IA n'est pas consciente
   - Toute «humilité» observée est comportementale et imposée par les concepteurs.

2. Dépendance au modèle sous-jacent
   - L'efficacité de l'injecteur dépend des capacités du LLM (compréhension d'instructions, suivi du contexte).

3. Biais d'injecteur
   - Si mal conçu, l'injecteur peut introduire ou amplifier des biais ; nécessité d'audits réguliers.

4. Mesures proxy pour énergie/stabilité
   - Actuellement estimées par temps d'exécution ou heuristiques ; mesures physiques recommandées (wattmètre).

5. Cryptage sémantique: limites
   - Watermark ≠ confidentialité ; nécessite chiffrement fort pour données sensibles.

6. Reproductibilité & audit
   - Nécessité d'artefacts, seeds, corpus standards; résultats doivent être validés par tiers.

7. Responsabilités légales
   - Publication doit respecter Zero‑Claim : aucun chiffre sans audit.
